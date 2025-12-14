from fastapi import FastAPI
from app.notes import services as notes_services
from app.notes.schemas import NoteCreate, NotePatch, NoteUpdate, NoteOut
from app.db.config import SessionDep

app = FastAPI()

# @app.post("/notes", response_model=NoteOut)
# async def create_note(new_note: NoteCreate,AsyncSession = Depends(get_db)):
#     note = await notes_services.create_note(new_note)
#     return note


@app.post("/notes", response_model=NoteOut)
async def create_note(session: SessionDep, new_note: NoteCreate):
    note = await notes_services.create_note(session, new_note)
    return note


@app.get("/notes", response_model=list[NoteOut])
async def get_notes_all(session: SessionDep):
    notes = await notes_services.get_notes(session)
    return notes


@app.get("/notes/{note_id}", response_model=NoteOut)
async def get_note(session: SessionDep, note_id: int):
    note = await notes_services.get_note(session, note_id)
    return note


@app.put("/notes/{note_id}", response_model=NoteOut)
async def update_note(session: SessionDep, note_id: int, note: NoteUpdate):
    note = await notes_services.update_notes(session, note_id, note)
    return note


@app.patch("/notes/{note_id}", response_model=NoteOut)
async def patch_note(session: SessionDep, note_id: int, note: NotePatch):
    note = await notes_services.patch_note(session, note_id, note)
    return note


@app.delete("/notes/{note_id}")
async def delete_note(session: SessionDep, note_id: int):
    note = await notes_services.delete_note(session, note_id)
    return note
