from fastapi import FastAPI
from app.account.routers import router as account_router

app = FastAPI(title="Ecommerce API", description="Ecommerce API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to Ecommerce API"}


app.include_router(account_router, prefix="/api/account", tags=["Account"])
