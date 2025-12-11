from fastapi import FastAPI
from app.user import services as user_services
from app.agents import services as agent_services
from pydantic import BaseModel

fastapi = FastAPI()


# User Model
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@fastapi.post("/users")
async def create_user(user: User):
    await user_services.create_user(
        name=user.name, email=user.email, password=user.password
    )
    return {"status": "success"}


@fastapi.get("/users")
async def get_all_users():
    users = await user_services.get_all_users()
    return {"status": "success", "data": users}


@fastapi.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    user = await user_services.get_user_by_id(user_id)
    return {"status": "success", "data": user}


@fastapi.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    await user_services.update_user(
        user_id=user_id, name=user.name, email=user.email, password=user.password
    )
    return {"status": "success"}


@fastapi.delete("/users/{user_id}")
async def delete_user(user_id: int):
    await user_services.delete_user(user_id)
    return {"status": "success"}


# Agent Model
class Agent(BaseModel):
    id: int
    name: str
    key: str
    status: str


@fastapi.post("/agents")
async def create_agent(agent: Agent):
    await agent_services.create_agent(
        name=agent.name, key=agent.key, status=agent.status
    )
    return {"status": "success"}


@fastapi.get("/agents")
async def get_all_agents():
    agents = await agent_services.get_all_agents()
    return {"status": "success", "data": agents}


@fastapi.get("/agents/{agent_id}")
async def get_agent_by_id(agent_id: int):
    agent = await agent_services.get_agent_by_id(agent_id)
    return {"status": "success", "data": agent}


@fastapi.put("/agents/{agent_id}")
async def update_agent(agent_id: int, agent: Agent):
    await agent_services.update_agent(
        agent_id=agent_id, name=agent.name, key=agent.key, status=agent.status
    )
    return {"status": "success"}


@fastapi.delete("/agents/{agent_id}")
async def delete_agent(agent_id: int):
    await agent_services.delete_agent(agent_id)
    return {"status": "success"}
