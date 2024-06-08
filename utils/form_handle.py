import json
from typing import Dict, Union, Optional

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from static.pydentic_models.pydentic import FormData

from utils.export_data import export_data as exp
router = APIRouter()


def load_data(path: str) -> dict | None:
    with open("data/data.json", 'r') as f:
        form_data: dict = json.load(f)
        try:
            form_data = form_data[path.split('/')[1]][path]
        except KeyError:
            return
        return form_data


def append_data(data: Dict[str, Union[Dict[str, str], str]], dir_: Optional[str] = None):
    with open("data/data.json", 'r') as f:
        json_data = json.load(f)
        if dir_:
            json_data[dir_].update(data)

        else:
            json_data.update(data)
    with open("data/data.json", 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


@router.post("/submit")
async def submit(data: FormData):
    # Process the form data here
    export = data.__root__.pop("export_")
    page_name = next(iter(data.__root__.keys()))
    dir_, page = page_name.lstrip('/').split('/')
    append_data(data.__root__, dir_)
    if export.lower() == "true":
        exp(dir_)

    return RedirectResponse(url=f"/{dir_+'/page'+str(int(page[4:])+1)}", status_code=303)


