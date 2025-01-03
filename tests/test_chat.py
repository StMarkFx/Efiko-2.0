from fastapi.testclient import TestClient
import pytest
from app.models.chat import ChatMessage

def test_chat_endpoint(client: TestClient):
    message = ChatMessage(
        content="Hello, how are you?",
        conversation_history=[],
        vectorstore_id=None
    )
    
    response = client.post("/api/v1/chat", json=message.dict())
    assert response.status_code == 200
    assert "content" in response.json()
    assert "timestamp" in response.json() 