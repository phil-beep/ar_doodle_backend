from typing import List
from pydantic import BaseModel

class Drawing(BaseModel):
    drawing: List[List[List[int]]]
