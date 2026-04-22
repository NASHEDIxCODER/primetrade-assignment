from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.task import Task
from app.core.deps import get_current_user , get_current_admin
from app.schemas.task import TaskCreate, TaskUpdate
from app.core.logging import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin/all")
def get_all_tasks(db: Session = Depends(get_db), admin= Depends(get_current_admin)):
    return db.query(Task).all()


@router.post("/")
def create_task(data: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = Task(title=data.title, description=data.description, owner_id=user.id)
    logger.info(f"User {user.id} created task {task.title}")
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/")
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Task).filter(Task.owner_id == user.id).all()



@router.put("/{task_id}")
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    logger.info(f"User {user.id} is updating task {task_id}")

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = data.title
    task.description = data.description
    task.is_done = data.is_done

    db.commit()
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    logger.info(f"User {user.id} is deleting task {task_id}")

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # allow owner OR admin
    if task.owner_id != user.id and user.role != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(task)
    db.commit()

    return {"msg": "Deleted"}