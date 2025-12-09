from app.db.base import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column


# Product Model
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    price: Mapped[float] = mapped_column(Float(10, 2))
    description: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price},description={self.description})"
