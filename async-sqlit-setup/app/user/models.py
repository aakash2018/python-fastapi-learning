from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)


def __repr__(self) -> str:
    return f"User(id={self.id}, name={self.name}, email={self.email}, password={self.password})"
