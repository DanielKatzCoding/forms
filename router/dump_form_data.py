from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# List to store quiz data
form_data_list = []


@router.post("/submit_form", response_class=HTMLResponse)
async def submit_form(request: Request, **kwargs):
    # Create a dictionary with the form data
    form_data = {
        'form_data': kwargs
    }

    # Append form data to the list
    form_data_list.append(form_data)

    # Write updated data back to JSON file
    with open('data/data.json', 'w') as file:
        json.dump(form_data_list, file, indent=4)

    # Prepare context to pass to template
    context = {
        "request": request,
        "message": "Form data submitted successfully!",
    }

    # Render the template with updated context (adjust as per your needs)
    return templates.TemplateResponse("page1.html", context)