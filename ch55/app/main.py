from fastapi import FastAPI
from app.user import services as user_services
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@app.post("/users")
def create_user(user: UserCreate):
    users = user_services.create_user(
        username=user.username, email=user.email, password=user.password
    )
    return users


@app.get("/users")
def get_all_users():
    users = user_services.get_all_users()
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_services.get_user(user_id)
    return user
