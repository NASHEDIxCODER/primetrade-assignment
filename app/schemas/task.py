from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str
    description: str
    is_done: bool