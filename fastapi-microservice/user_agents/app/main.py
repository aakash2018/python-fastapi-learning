from fastapi import FastAPI
from user_agents.app.router.router import router
from contextlib import asynccontextmanager
from .db.config import create_tables, engine
from sqlmodel import SQLModel
# from .models import UserAgent

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


user_app = FastAPI(lifespan=lifespan, title="User Agents Service", version="1.0.0")
user_app.include_router(router)
