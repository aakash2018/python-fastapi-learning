from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int
    name: str
