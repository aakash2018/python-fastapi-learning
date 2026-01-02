from app.account.models import User, RefreshToken
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.account.schemas import UserCreate
from app.account.utils import hash_password


async def create_user(session: AsyncSession, user: UserCreate):
    print("create user works")
    stmt = select(User).where(User.email == user.email)
    result = await session.execute(stmt)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    new_user = User(email=user.email, hashed_password=hash_password(user.password))
    try:
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
    except Exception:
        await session.rollback()
        raise
    return new_user
