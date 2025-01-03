import pytest
from fastapi.testclient import TestClient
from pathlib import Path

def test_document_upload(client: TestClient):
    test_file_path = Path(__file__).parent / "test_files" / "test.pdf"
    
    with open(test_file_path, "rb") as f:
        response = client.post(
            "/api/v1/documents/upload",
            files={"file": ("test.pdf", f, "application/pdf")}
        )
    
    assert response.status_code == 200
    assert response.json()["message"] == "Document processed successfully" 