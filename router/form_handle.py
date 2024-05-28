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
    return RedirectResponse(url=f"/page{int(page_name[4:])+1}", status_code=303)


