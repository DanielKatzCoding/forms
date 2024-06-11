import json
from typing import Dict, Union, Optional

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from static.pydentic_models.pydentic import FormData

from utils.finalizing import export_data as exp
router = APIRouter()


def get_form_data(path: str) -> dict | None:
    with open("data/data.json", 'r') as f:
        form_data: dict = json.load(f)
        print(path)
        return form_data.get(path)


def update_data(data: Dict[str, Union[Dict[str, str], str]]):
    with open("data/data.json", 'r') as f:
        json_data = json.load(f)

    json_data.update(data)

    with open("data/data.json", 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


@router.post("/submit")
async def submit(data: FormData):
    # Process the form data here
    export = data.__root__.pop("export_")
    page_name = next(iter(data.__root__.keys()))
    dir_, page = page_name.lstrip('/').split('/')
    update_data(data.__root__)
    if export.lower() == "true":
        exp()
        return RedirectResponse(url="/", status_code=303)

    return RedirectResponse(url=f"/{dir_+'/page'+str(int(page[4:])+1)}", status_code=303)


