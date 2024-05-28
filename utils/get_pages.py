from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse

router = APIRouter()

# Initialize templates
templates = Jinja2Templates(directory="templates")


def add_routes(directory):
    templates_path = Path(directory)
    for template_file in templates_path.glob("*.html"):
        route_path = f"/{template_file.stem}"

        async def route_func(request: Request, template_name=template_file.name):
            return templates.TemplateResponse(template_name, {"request": request})

        router.add_api_route(route_path, route_func, methods=["GET"])


# Add routes for all templates in the "templates" directory
add_routes("templates")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
