import json
from typing import Dict

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from static.pydentic_models.pydentic import FormData

router = APIRouter()


def append_data(data: Dict[str, Dict[str, str]]):
    with open("data/data.json", 'r') as f:
        json_data = json.load(f)
    json_data.update(data)
    with open("data/data.json", 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


@router.post("/submit")
async def submit(data: FormData):
    # Process the form data here
    print(f"Received data: {data.__root__}")
    page_name = next(iter(data.__root__.keys()))
    print(page_name)
    append_data(data.__root__)
    return RedirectResponse(url=f"/page{int(page_name[4:])+1}", status_code=303)


