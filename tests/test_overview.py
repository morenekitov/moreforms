from fastapi.testclient import TestClient

from app.main import app


def test_overview_endpoint_returns_metrics_payload() -> None:
    with TestClient(app) as client:
        response = client.get("/overview", headers={"x-auth-request-email": "member@example.com"})
        assert response.status_code == 200
        payload = response.json()
        assert "hypotheses_total" in payload
        assert "interviews_total" in payload
        assert "insights_total" in payload
        assert "signals_total" in payload
        assert "latest_changes" in payload
