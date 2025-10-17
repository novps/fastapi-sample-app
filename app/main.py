from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from .database import Base, engine, get_session
from . import crud, schemas


# === Lifespan event ===
@asynccontextmanager
async def lifespan(app: FastAPI):
    # При запуске
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # При завершении — можно закрывать соединения, чистить ресурсы и т.д.


app = FastAPI(
    title="NoVPS To-Do App",
    lifespan=lifespan,
)

templates = Jinja2Templates(directory="app/templates")


# === Frontend ===
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# === API ===
@app.get("/todos", response_model=list[schemas.TodoRead])
async def list_todos(db: AsyncSession = Depends(get_session)):
    return await crud.get_todos(db)


@app.post("/todos", response_model=schemas.TodoRead)
async def add_todo(todo: schemas.TodoCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_todo(db, todo)


@app.patch("/todos/{todo_id}", response_model=schemas.TodoRead)
async def toggle_todo(todo_id: int, data: schemas.TodoUpdate, db: AsyncSession = Depends(get_session)):
    todo = await crud.update_todo(db, todo_id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.delete("/todos/{todo_id}")
async def remove_todo(todo_id: int, db: AsyncSession = Depends(get_session)):
    todo = await crud.delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Deleted"}
