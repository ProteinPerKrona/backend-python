# Imports
from pydantic import BaseModel


class Request(BaseModel):
    '''
    A request class following the following form\n
    Example request to filter for more than 10% protein and order by fat percentege:\n
    {\t"orderby": "nutritions.fett",\n
        "filter": {\t"nutritions.protein":{\t"$gt":10}\t}\n
    }
    '''
    filter: dict | None = None
    orderby: str | None = None
