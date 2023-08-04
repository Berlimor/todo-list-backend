from sqlalchemy.orm import Session

from . import schemas, models

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoBase):
    db_todo = models.Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    
    return db_todo
    
def update_todo_status(db: Session, id: int):
    todo = db.query(models.Todo).get(id)
    if todo.status:
        todo.status = False
    else:
        todo.status = True
    db.commit()
    return todo