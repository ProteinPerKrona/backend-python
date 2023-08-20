# Imports
from pydantic import BaseModel

class Request(BaseModel):
    filter:dict | None=None
    orderby:str | None=None
