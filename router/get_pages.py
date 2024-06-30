import json
from pathlib import Path
import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from utils.form_handle import get_form_data
from utils.finalizing import reset_database
from functools import lru_cache

router = APIRouter()

# Initialize templates to point to the root of your templates directory
templates = Jinja2Templates(directory="templates")


@lru_cache(maxsize=1)
def add_routes(directory, prefix):
    templates_path = Path(directory)
    with open("data/default.json", 'r') as f:
        count = len(json.load(f)[prefix[1:]]["navs"])
    lst_pages = [f"page{i}" for i in range(1, count+1)]
    dict_pages = {"pages": [f"{prefix}/{page}" for page in lst_pages]}

    for template_file in lst_pages:
        route_path = f"{prefix}/{template_file}"
        tmp_data = dict_pages.copy()

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
add_routes("templates/interviewer_feedback", "/interviewer_feedback")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    reset_database()
    return templates.TemplateResponse("index.html", {"request": request})
