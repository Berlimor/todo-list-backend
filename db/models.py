from sqlalchemy import Boolean, Column, String, Integer

from .database import Base

class Todo(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(Boolean, default=False)