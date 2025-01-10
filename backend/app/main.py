from fastapi import FastAPI

from .database import engine

engine.connect()
app = FastAPI()
