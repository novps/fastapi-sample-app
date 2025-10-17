from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from . import models, schemas


async def get_todos(db: AsyncSession):
    result = await db.execute(select(models.Todo).order_by(models.Todo.id.desc()))
    return result.scalars().all()


async def create_todo(db: AsyncSession, todo: schemas.TodoCreate):
    new_todo = models.Todo(title=todo.title)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


async def update_todo(db: AsyncSession, todo_id: int, data: schemas.TodoUpdate):
    result = await db.execute(select(models.Todo).filter_by(id=todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        return None
    todo.completed = data.completed
    await db.commit()
    await db.refresh(todo)
    return todo


async def delete_todo(db: AsyncSession, todo_id: int):
    result = await db.execute(select(models.Todo).filter_by(id=todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        return None
    await db.delete(todo)
    await db.commit()
    return todo
