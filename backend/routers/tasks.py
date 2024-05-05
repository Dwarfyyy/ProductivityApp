from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Task

router = APIRouter()

fake_tasks_db = [{"id": 1, "title": "Task 1"}, {"id": 2, "title": "Task 2"}]

@router.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return fake_tasks_db

@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    task = next((task for task in fake_tasks_db if task["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
