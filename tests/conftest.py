import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import Settings

@pytest.fixture
def test_settings():
    return Settings(
        GEMINI_API_KEY="test_key",
        SECRET_KEY="test_secret",
        TESTING=True
    )

@pytest.fixture
def client(test_settings):
    app.dependency_overrides[Settings] = lambda: test_settings
    with TestClient(app) as test_client:
        yield test_client
