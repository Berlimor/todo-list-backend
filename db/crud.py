from sqlalchemy.orm import Session

from . import shemas, models

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: shemas.TodoBase):
    db_todo = models.Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    
    return db_todo
    