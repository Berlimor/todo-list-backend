from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class Todo(TodoBase):
    id: int
    status: bool = False

    class Config:
        orm_mode = True