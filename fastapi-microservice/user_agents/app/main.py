from fastapi import FastAPI
from user_agents.app.router.router import router

user_app = FastAPI(title="user-agents")
user_app.include_router(router)
