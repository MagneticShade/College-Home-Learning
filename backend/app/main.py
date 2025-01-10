from fastapi import FastAPI

from .database import engine
from .database.models import SQLModel

SQLModel.metadata.create_all(engine)
app = FastAPI()
