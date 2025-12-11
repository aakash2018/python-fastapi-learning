from app.db.config import async_session
from app.user.models import User
from sqlalchemy import select, insert, update, delete


async def create_user(name: str, email: str, password: str):
    async with async_session() as session:
        async with session.begin():
            user = User(name=name, email=email, password=password)
            session.add(user)
            await session.commit()
    return user


async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def get_user_by_id(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()


async def update_user(user_id: int, name: str, email: str, password: str):
    async with async_session() as session:
        async with session.begin():
            user = await session.execute(select(User).where(User.id == user_id))
            user = user.scalar_one_or_none()
            if user:
                user.name = name
                user.email = email
                user.password = password
    return user


async def delete_user(user_id: int):
    async with async_session() as session:
        async with session.begin():
            user = await session.execute(select(User).where(User.id == user_id))
            user = user.scalar_one_or_none()
            if user:
                session.delete(user)
    return user
