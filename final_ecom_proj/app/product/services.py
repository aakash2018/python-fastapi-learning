from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.product.models import Category, Product
from app.product.schemas import CategoryCreate, CategoryOut
from app.db.config import SessionDep


async def create_category(session: SessionDep, category: CategoryCreate) -> CategoryOut:
    category = Category(name=category.name)
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category


async def get_all_categories(session: SessionDep) -> list[CategoryOut]:
    stmt = select(Category)
    result = await session.scalars(stmt)
    return result.all()
