import string
from typing import List
from pydantic import BaseModel

class Drawing(BaseModel):
    drawing: List[List[List[int]]]

class File_path(BaseModel):
    imageLocation: str
