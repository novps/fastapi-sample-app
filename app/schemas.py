from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: str


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    completed: bool


class TodoRead(TodoBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
