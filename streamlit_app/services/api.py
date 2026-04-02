import os

import requests


API_BASE_URL = os.getenv("STREAMLIT_API_BASE_URL", "http://localhost:8000").rstrip("/")
TIMEOUT_SECONDS = 15


class ApiError(RuntimeError):
    pass


def get_json(path: str, params: dict | None = None) -> list | dict:
    url = f"{API_BASE_URL}{path}"
    response = requests.get(url, params=params, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def safe_get(path: str, params: dict | None = None) -> tuple[bool, list | dict | None, str | None]:
    try:
        return True, get_json(path, params=params), None
    except requests.RequestException as exc:
        return False, None, str(exc)
