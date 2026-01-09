from fastapi import APIRouter, Depends, HTTPException, status
from app.account.models import User
from app.product.services import create_category, get_all_categories
from app.product.schemas import CategoryCreate, CategoryOut
from app.db.config import SessionDep
from app.account.deps import require_admin


router = APIRouter()


@router.post("/", response_model=CategoryOut)
async def category_create(
    session: SessionDep,
    category: CategoryCreate,
    admin_user: User = Depends(require_admin),
):
    return await create_category(session, category)


@router.get("/", response_model=list[CategoryOut])
async def list_categories(session: SessionDep):
    return await get_all_categories(session)
