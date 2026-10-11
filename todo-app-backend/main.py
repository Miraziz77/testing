from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)


book = []


class TaskSchema(BaseModel):
    id: str
    title: str
    completed: bool


class TaskCreateSchema(BaseModel):
    title: str



class Book(BaseModel):
    title: str


tasks: list[TaskSchema] = []



@app.get("/book")
def return_book(new_book: Book):
    return {"message": f'Любимая книга: {new_book}'}


@app.get("/tasks")
def get_tasks() -> list[TaskSchema]:
    return tasks



@app.post("/tasks")
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4()), title=payload.title, completed=False)

    tasks.append(new_task)
    return new_task





@app.post("/book")
def add_book(new_book: Book):
    book.append(new_book)
    return {"status": "ok"}



