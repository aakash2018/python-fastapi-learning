from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


# creating dependency function
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# create a type alias
CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/products")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/orders")
async def read_users(commons: CommonsDep):
    return commons


# hierarchical dependencies
async def user_auth():
    return {"user_id": 1}


async def user_role(user_auth: Annotated[dict, Depends(user_auth)]):
    return {"user_id": user_auth["user_id"], "role": "admin"}


@app.get("/admin")
async def admin_only(role: Annotated[dict, Depends(user_role)]):
    return role
