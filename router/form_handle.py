from fastapi import APIRouter, Form, Request, Response
from static.pydentic_models.pydentic import FormData
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict
import json
from fastapi.responses import RedirectResponse

router = APIRouter()


def append_data(data: Dict[str, Dict[str, str]]):
    json_data = None
    with open("data/data.json", 'r') as f:
        json_data = json.load(f)
    json_data.update(data)
    with open("data/data.json", 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


@router.post("/submit")
async def submit(data: FormData):
    # Process the form data here
    print(f"Received data: {data.__root__}")
    page_name = data.__root__.pop("page_name")
    append_data(data.__root__)
    return RedirectResponse(url=f"/page{int(page_name[4:])+1}")

# @router.post("/submit_form", response_class=HTMLResponse)
# async def submit_form(request: Request, **kwargs):
#     # Create a dictionary with the form data
#     form_data = {
#         'form_data': kwargs
#     }
#
#     # Append form data to the list
#     form_data_list.append(form_data)
#
#     # Write updated data back to JSON file
#     with open('data/data.json', 'w') as file:
#         json.dump(form_data_list, file, indent=4)
#
#     # Prepare context to pass to template
#     context = {
#         "request": request,
#         "message": "Form data submitted successfully!",
#     }
#
#     # Render the template with updated context (adjust as per your needs)
#     return templates.TemplateResponse("page1.html", context)