"""Tests for the FastAPI notes demo."""

import pytest
from fastapi.testclient import TestClient

from demos.fastapi_demo import app as app_module
from demos.fastapi_demo.app import app


@pytest.fixture()
def client() -> TestClient:
    """Provide a TestClient and reset in-memory state before each test."""
    app_module._notes.clear()
    app_module._reset_id_counter()
    with TestClient(app) as c:
        yield c
    app_module._notes.clear()


class TestMeta:
    """Tests for meta endpoints."""

    def test_root(self, client: TestClient) -> None:
        resp = client.get("/")
        assert resp.status_code == 200
        body = resp.json()
        assert body["message"] == "FastAPI Notes Demo"
        assert body["docs"] == "/docs"

    def test_health(self, client: TestClient) -> None:
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}


class TestListNotes:
    """Tests for GET /notes."""

    def test_seeded_note_present(self, client: TestClient) -> None:
        resp = client.get("/notes")
        assert resp.status_code == 200
        notes = resp.json()
        assert len(notes) == 1
        assert notes[0]["title"] == "Welcome to FastAPI"

    def test_pagination_skip(self, client: TestClient) -> None:
        # Create two extra notes so we have 3 total.
        client.post("/notes", json={"title": "A"})
        client.post("/notes", json={"title": "B"})
        resp = client.get("/notes", params={"skip": 1, "limit": 1})
        assert resp.status_code == 200
        notes = resp.json()
        assert len(notes) == 1

    def test_pagination_limit(self, client: TestClient) -> None:
        for i in range(5):
            client.post("/notes", json={"title": f"Note {i}"})
        resp = client.get("/notes", params={"limit": 3})
        assert resp.status_code == 200
        assert len(resp.json()) == 3

    def test_invalid_limit_rejected(self, client: TestClient) -> None:
        resp = client.get("/notes", params={"limit": 0})
        assert resp.status_code == 422


class TestGetNote:
    """Tests for GET /notes/{id}."""

    def test_get_existing(self, client: TestClient) -> None:
        resp = client.get("/notes/1")
        assert resp.status_code == 200
        assert resp.json()["title"] == "Welcome to FastAPI"

    def test_get_missing_returns_404(self, client: TestClient) -> None:
        resp = client.get("/notes/999")
        assert resp.status_code == 404
        assert "999" in resp.json()["detail"]


class TestCreateNote:
    """Tests for POST /notes."""

    def test_create_returns_201(self, client: TestClient) -> None:
        resp = client.post("/notes", json={"title": "New", "content": "Body"})
        assert resp.status_code == 201
        body = resp.json()
        assert body["title"] == "New"
        assert body["content"] == "Body"
        assert isinstance(body["id"], int)
        assert "created_at" in body
        assert "updated_at" in body

    def test_create_empty_title_rejected(self, client: TestClient) -> None:
        resp = client.post("/notes", json={"title": ""})
        assert resp.status_code == 422

    def test_create_missing_title_rejected(self, client: TestClient) -> None:
        resp = client.post("/notes", json={"content": "no title"})
        assert resp.status_code == 422

    def test_create_long_title_rejected(self, client: TestClient) -> None:
        resp = client.post("/notes", json={"title": "x" * 201})
        assert resp.status_code == 422


class TestUpdateNote:
    """Tests for PUT /notes/{id}."""

    def test_update_title(self, client: TestClient) -> None:
        resp = client.put("/notes/1", json={"title": "Updated"})
        assert resp.status_code == 200
        body = resp.json()
        assert body["title"] == "Updated"
        # content should be unchanged
        assert body["content"] == "This is a sample note created on startup."

    def test_update_content(self, client: TestClient) -> None:
        resp = client.put("/notes/1", json={"content": "New body"})
        assert resp.status_code == 200
        assert resp.json()["content"] == "New body"

    def test_update_missing_returns_404(self, client: TestClient) -> None:
        resp = client.put("/notes/999", json={"title": "x"})
        assert resp.status_code == 404


class TestDeleteNote:
    """Tests for DELETE /notes/{id}."""

    def test_delete_returns_204(self, client: TestClient) -> None:
        resp = client.delete("/notes/1")
        assert resp.status_code == 204
        assert resp.content == b""

    def test_delete_then_get_404(self, client: TestClient) -> None:
        client.delete("/notes/1")
        resp = client.get("/notes/1")
        assert resp.status_code == 404

    def test_delete_missing_returns_404(self, client: TestClient) -> None:
        resp = client.delete("/notes/999")
        assert resp.status_code == 404
