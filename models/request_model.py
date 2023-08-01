# Imports
from pydantic import BaseModel

class Request(BaseModel):
    ppk:float | None = None
    protein:float | None = None