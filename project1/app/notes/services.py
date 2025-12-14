from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import NoteCreate, NotePatch, NoteUpdate, NoteOut
from sqlalchemy.ext.asyncio import AsyncSession


async def create_note(session: AsyncSession, note: NoteCreate):
    note = Note(title=note.title, content=note.content)
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note


async def get_note(session: AsyncSession, note_id: int):
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


async def get_notes(session: AsyncSession):
    notes = await session.execute(select(Note))
    return notes.scalars().all()


async def update_notes(session: AsyncSession, note_id: int, new_note: NoteUpdate):
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = new_note.title
    note.content = new_note.content
    await session.commit()
    await session.refresh(note)
    return note


async def patch_note(session: AsyncSession, note_id: int, new_note: NotePatch):
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if note.title is not None:
        note.title = new_note.title
    if note.content is not None:
        note.content = new_note.content

    await session.commit()
    await session.refresh(note)
    return note


async def delete_note(session: AsyncSession, note_id: int):
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    await session.delete(note)
    await session.commit()
    return {"message": "Note deleted successfully"}
