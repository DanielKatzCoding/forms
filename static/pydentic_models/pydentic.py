from pydantic import BaseModel
from typing import Dict, Union


class FormData(BaseModel):
    __root__: Dict[str, Union[Dict[str, str], str]]
