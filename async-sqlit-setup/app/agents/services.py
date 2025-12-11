from app.db.config import async_session
from app.agents.models import Agent
from sqlalchemy import select, insert, update, delete


async def create_agent(name: str, key: str, status: str):
    async with async_session() as session:
        async with session.begin():
            agent = Agent(name=name, key=key, status=status)
            session.add(agent)
            return agent


async def get_all_agents():
    async with async_session() as session:
        async with session.begin():
            agents = session.execute(select(Agent)).all()
            return agents


async def get_agent_by_id(id: int):
    async with async_session() as session:
        async with session.begin():
            agent = session.execute(
                select(Agent).where(Agent.id == id)
            ).scalar_one_or_none()
            return agent


async def update_agent(id: int, name: str, key: str, status: str):
    async with async_session() as session:
        async with session.begin():
            agent = session.execute(
                select(Agent).where(Agent.id == id)
            ).scalar_one_or_none()
            if agent:
                agent.name = name
                agent.key = key
                agent.status = status
                return agent


async def delete_agent(id: int):
    async with async_session() as session:
        async with session.begin():
            agent = session.execute(
                select(Agent).where(Agent.id == id)
            ).scalar_one_or_none()
            if agent:
                session.delete(agent)
                return agent


async def change_status(id: int, status: str):
    async with async_session() as session:
        async with session.begin():
            agent = session.execute(
                select(Agent).where(Agent.id == id)
            ).scalar_one_or_none()
            if agent:
                agent.status = status
                return agent
