"""Script to create MongoDB indexes for the core collections."""
import asyncio
from app.db import get_client, DB_NAME

async def create_indexes():
    client = get_client()
    db = client[DB_NAME]
    await db["tenants"].create_index("tenant_id", unique=True)
    await db["users"].create_index([("tenant_id", 1), ("user_id", 1)], unique=True)
    await db["chat_sessions"].create_index([("tenant_id", 1), ("user_id", 1)])
    await db["messages"].create_index([("tenant_id", 1), ("session_id", 1)])
    await db["use_cases"].create_index([("tenant_id", 1), ("id", 1)])

if __name__ == "__main__":
    asyncio.run(create_indexes())
