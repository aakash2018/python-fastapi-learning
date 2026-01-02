from pydantic import BaseModel, EmailStr, constr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_admin: bool = False
    is_verified: bool = False


class UserCreate(UserBase):
    password: constr(min_length=8, max_length=72)


class UserUpdate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    model_config = {"from_attributes": True}


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
