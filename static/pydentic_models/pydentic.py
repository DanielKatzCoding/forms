from typing import Dict, Union

from pydantic import BaseModel


class FormData(BaseModel):
    __form_data__: Dict[str, Union[Dict[str, str], str]]
