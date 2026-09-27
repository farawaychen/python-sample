"""FastAPI demo: a small in-memory notes API.

This demo covers the core FastAPI concepts:
- Pydantic models for request/response validation
- Path and query parameters
- CRUD operations (Create / Read / Update / Delete)
- HTTP status codes and error handling
- Lifespan events (startup / shutdown)
- Automatic OpenAPI docs at /docs

Run it:
    uv run uvicorn demos.fastapi_demo.app:app --reload

Then open http://127.0.0.1:8000/docs in your browser.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------


class NoteCreate(BaseModel):
    """Payload for creating a new note."""

    title: str = Field(..., min_length=1, max_length=200, description="Note title")
    content: str = Field(default="", description="Note body")


class NoteUpdate(BaseModel):
    """Payload for updating an existing note (all fields optional)."""

    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None)


class Note(BaseModel):
    """A note as returned by the API."""

    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


# ---------------------------------------------------------------------------
# In-memory storage
# ---------------------------------------------------------------------------

_notes: dict[int, Note] = {}
# Mutable holder so all references (routes, lifespan, tests) share one object.
_next_id: list[int] = [1]


def _reset_id_counter() -> None:
    """Reset the id counter back to 1 (used by tests)."""
    _next_id[0] = 1


# ---------------------------------------------------------------------------
# Lifespan (startup / shutdown)
# ---------------------------------------------------------------------------


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Seed a sample note on startup; clean up on shutdown."""
    _notes.clear()
    _reset_id_counter()
    now = datetime.now(UTC)
    _notes[1] = Note(
        id=1,
        title="Welcome to FastAPI",
        content="This is a sample note created on startup.",
        created_at=now,
        updated_at=now,
    )
    # Advance the counter so the first created note gets id=2, not id=1.
    _next_id[0] = 2
    yield
    _notes.clear()


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = FastAPI(
    title="FastAPI Notes Demo",
    description="A minimal in-memory notes API demonstrating FastAPI basics.",
    version="0.1.0",
    lifespan=lifespan,
    # When served behind a reverse proxy that mounts the app under a
    # path prefix (e.g. /proxy/8000), set this so the generated
    # OpenAPI spec and Swagger UI use the correct base URL.
    # root_path="/proxy/8000",
)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/", tags=["meta"])
def root() -> dict[str, str]:
    """Landing page pointing to the docs."""
    return {"message": "FastAPI Notes Demo", "docs": "/docs"}


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    """Simple health-check endpoint."""
    return {"status": "ok"}


@app.get("/notes", response_model=list[Note], tags=["notes"])
def list_notes(
    skip: int = Query(default=0, ge=0, description="Number of notes to skip"),
    limit: int = Query(default=100, ge=1, le=1000, description="Max notes to return"),
) -> list[Note]:
    """List notes with simple pagination."""
    items = list(_notes.values())
    return items[skip : skip + limit]


@app.get("/notes/{note_id}", response_model=Note, tags=["notes"])
def get_note(note_id: int) -> Note:
    """Fetch a single note by id."""
    note = _notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
    return note


@app.post("/notes", response_model=Note, status_code=201, tags=["notes"])
def create_note(payload: NoteCreate) -> Note:
    """Create a new note."""
    now = datetime.now(UTC)
    note = Note(
        id=_next_id[0],
        title=payload.title,
        content=payload.content,
        created_at=now,
        updated_at=now,
    )
    _next_id[0] += 1
    _notes[note.id] = note
    return note


@app.put("/notes/{note_id}", response_model=Note, tags=["notes"])
def update_note(note_id: int, payload: NoteUpdate) -> Note:
    """Update an existing note (partial update supported)."""
    note = _notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if payload.title is not None:
        note.title = payload.title
    if payload.content is not None:
        note.content = payload.content
    note.updated_at = datetime.now(UTC)
    return note


@app.delete("/notes/{note_id}", status_code=204, tags=["notes"])
def delete_note(note_id: int) -> None:
    """Delete a note."""
    if note_id not in _notes:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
    del _notes[note_id]


# ---------------------------------------------------------------------------
# Entry point (for `uv run python -m demos.fastapi_demo.app`)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
