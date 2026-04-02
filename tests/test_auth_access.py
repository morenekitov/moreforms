from fastapi.testclient import TestClient

from app.main import app


def test_allowed_user_can_access_me() -> None:
    with TestClient(app) as client:
        response = client.get("/me", headers={"x-auth-request-email": "member@example.com"})
        assert response.status_code == 200
        payload = response.json()
        assert payload["email"] == "member@example.com"
        assert payload["is_authenticated"] is True


def test_owner_can_read_allowed_emails() -> None:
    with TestClient(app) as client:
        response = client.get("/auth/allowed-emails", headers={"x-auth-request-email": "owner@example.com"})
        assert response.status_code == 200
        emails = response.json()["emails"]
        assert "owner@example.com" in emails
        assert "member@example.com" in emails


def test_non_whitelisted_user_is_rejected() -> None:
    with TestClient(app) as client:
        response = client.get("/me", headers={"x-auth-request-email": "outsider@example.com"})
        assert response.status_code == 403
