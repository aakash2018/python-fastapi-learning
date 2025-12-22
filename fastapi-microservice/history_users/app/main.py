from fastapi import FastAPI
from history_users.app.router.router import router

history_app = FastAPI(title="history")
history_app.include_router(router)
