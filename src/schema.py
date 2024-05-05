from pydantic import BaseModel

class bookbase(BaseModel):
    title : str
    author : str
    year  : int
    isbn  : str