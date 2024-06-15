import json
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils.form_handle import get_form_data
from utils.finalizing import reset_database

router = APIRouter()

# Initialize templates to point to the root of your templates directory
templates = Jinja2Templates(directory="templates")


def add_routes(directory, prefix):
    templates_path = Path(directory)
    lst_pages = sorted([t_path for t_path in templates_path.glob("*.html")])
    dict_pages = {"pages": [f"{prefix}/{page.name.rsplit('.')[0]}" for page in lst_pages]}

    for template_file in lst_pages:
        route_path = f"{prefix}/{template_file.stem}"
        tmp_data = dict_pages.copy()

        # with open("data/data.json", 'r') as f:
        #     tmp_data["pages"] = json.load(f)
        #     tmp_data.update(json.load(f))

        with open("data/default.json", 'r') as f:
            tmp_data["navs"] = json.load(f)[prefix.lstrip('/')]["navs"]

        async def route_func(request: Request, template_name=route_path):
            return templates.TemplateResponse(
                *[template_name + ".html", {
                    "request": request,
                    "data": tmp_data,
                    "form_data": get_form_data(template_name),
                    "zip": zip,
                    "range": range
                }]
            )

        router.add_api_route(route_path, route_func, methods=["GET"])


# Add routes for all templates in the "dynamics" directory
add_routes("templates/dynamics", "/dynamics")
add_routes("templates/interview", "/interview")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    reset_database()
    return templates.TemplateResponse("index.html", {"request": request})
