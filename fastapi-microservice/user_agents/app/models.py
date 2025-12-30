from sqlmodel import SQLModel, Field, UniqueConstraint
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import Column


class UserBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    description: Optional[str] = None
    text: Optional[str] = None

    is_active: bool = Field(default=True)
    status: str = Field(default="active")


class UserAgentCreate(UserBase):
    pass


class UserAgentOut(UserBase):
    pass  # id already inherited from UserBase


class UserAgent(UserBase, table=True):
    __tablename__ = "user_agents"
    __table_args__ = (
        UniqueConstraint("username"),
        UniqueConstraint("email"),
    )

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
