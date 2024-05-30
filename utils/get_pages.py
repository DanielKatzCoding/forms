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
    for template_file in templates_path.glob("*.html"):
        route_path = f"{prefix}/{template_file.stem}"
        print(template_file.name)

        with open("data/data.json", 'r') as f:
            data = json.load(f)
            data["quest"] = prefix
            print(data)
        async def route_func(request: Request, template_name=template_file.name):
            return templates.TemplateResponse(f"{prefix}/{template_name}", {"request": request, "data": data})

        router.add_api_route(route_path, route_func, methods=["GET"])


# Add routes for all templates in the "dynamics" directory
add_routes("templates/dynamics", "/dynamics")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
