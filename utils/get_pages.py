import json
from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Initialize templates to point to the root of your templates directory
templates = Jinja2Templates(directory="templates")


def add_routes(directory, prefix):
    templates_path = Path(directory)
    lst_pages = [page for page in templates_path.glob("*.html")]
    dict_pages = {"pages": [f"{prefix}/{page.name.rsplit('.')[0]}" for page in lst_pages]}

    for template_file in lst_pages:
        route_path = f"{prefix}/{template_file.stem}"
        print(route_path)
        tmp_data = dict_pages.copy()

        with open("data/data.json", 'r') as f:
            tmp_data.update(json.load(f)[prefix.lstrip('/')])

        async def route_func(request: Request):
            return templates.TemplateResponse(route_path + ".html", {"request": request, "data": tmp_data,"zip": zip})

        router.add_api_route(route_path, route_func, methods=["GET"])


# Add routes for all templates in the "dynamics" directory
add_routes("templates/dynamics", "/dynamics")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
