from pydantic import BaseModel
from typing import Dict


class FormData(BaseModel):
    __root__: Dict[str, str]