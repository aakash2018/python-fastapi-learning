from pydantic import BaseModel, ConfigDict
from typing import Optional


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class NotePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class NoteOut(NoteBase):
    model_config = ConfigDict(from_attributes=True)
