from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base


class StatusEnum(Enum):
    pending = "pending"
    running = "running"
    active = "active"
    deactive = "deactive"


# Agent Model
class Agent(Base):
    __tablename__ = "agents"
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    key = mapped_column(String)
    status = mapped_column(String, default=StatusEnum.active)


def __repr__(self) -> str:
    return (
        f"Agent(id={self.id}, name={self.name}, key={self.key}, status={self.status})"
    )
