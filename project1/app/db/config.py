from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import os
from fastapi import Depends
from typing import Annotated

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)


# both same dependency indextion to open and close session
async def get_db():
    session = async_session()
    print(f"Creating new AsyncSession: {id(session)}")
    try:
        async with session:
            yield session
        print(f"Session committed and closed: {id(session)}")
    except Exception as e:
        print(f"Error in session: {id(session)}, rolling back: {str(e)}")
        await session.rollback()
        raise
    finally:
        await session.close()
        print(f"Session explicitly closed: {id(session)}")


SessionDep = Annotated[AsyncSession, Depends(get_db)]
