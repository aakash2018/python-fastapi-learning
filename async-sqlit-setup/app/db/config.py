from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASE_PATH = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)
