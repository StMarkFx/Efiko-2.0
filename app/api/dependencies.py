from fastapi import Depends
from app.core.config import Settings
from app.services.chat_service import ChatService
from app.services.document_service import DocumentProcessor

def get_settings():
    return Settings()

def get_chat_service(settings: Settings = Depends(get_settings)):
    return ChatService(api_key=settings.GEMINI_API_KEY)

def get_document_processor():
    return DocumentProcessor()
