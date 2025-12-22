from fastapi import FastAPI
from history_users.app.main import history_app
from user_agents.app.main import user_app


gateway_app = FastAPI(title="API Gateway")


gateway_app.mount("/history", history_app)
gateway_app.mount("/useragent", user_app)
