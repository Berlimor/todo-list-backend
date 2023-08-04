from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from db import crud, models, shemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/", response_model=shemas.Todo)
def create_todo(todo: shemas.TodoBase, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/", response_model=list[shemas.Todo])
def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db=db)