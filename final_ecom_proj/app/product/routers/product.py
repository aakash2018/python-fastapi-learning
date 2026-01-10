from typing import Annotated
from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile, status
from app.product.services import create_product
from app.product.schemas import ProductCreate, ProductOut
from app.db.config import SessionDep
from app.account.deps import require_admin
from app.account.models import User
from app.product.models import Product

router = APIRouter()


@router.post("/", response_model=ProductOut)
async def product_create(
    session: SessionDep,
    title: str = Form(...),
    description: str | None = Form(None),
    price: float = Form(...),
    stock_quantity: int = Form(...),
    category_ids: Annotated[list[int], Form()] = [],
    image: UploadFile | None = File(None),
    admin_user: User = Depends(require_admin),
):
    product = ProductCreate(
        title=title,
        description=description,
        price=price,
        stock_quantity=stock_quantity,
        category_ids=category_ids,
    )
    return await create_product(session, product, image)
