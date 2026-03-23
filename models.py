from pydantic import BaseModel

class MoveAction(BaseModel):
    row: int
    col: int