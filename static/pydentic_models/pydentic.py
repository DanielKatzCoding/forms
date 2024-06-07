from typing import Dict, Union

from pydantic import BaseModel


class FormData(BaseModel):
    __root__: Dict[str, Union[Dict[str, str], str]]
