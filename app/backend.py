from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

from app.services.document_service import DocumentProcessor
from app.services.chat_service import ChatService
from app.models.chat import ChatMessage, ChatResponse
from app.config import Settings

# Load environment variables
load_dotenv()
settings = Settings()

# Initialize FastAPI app
app = FastAPI(
    title="Efiko API",
    description="Backend API for Efiko - Your Study Companion",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
document_processor = DocumentProcessor()
chat_service = ChatService(api_key=settings.GEMINI_API_KEY)

@app.post("/api/upload-document")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a document"""
    try:
        vectorstore = await document_processor.process_document(file)
        return {"message": "Document processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/chat")
async def chat(message: ChatMessage):
    """Process a chat message and return response"""
    try:
        response = await chat_service.get_response(
            message.content,
            message.conversation_history,
            message.vectorstore_id
        )
        return ChatResponse(
            content=response,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/export-chat/{chat_id}")
async def export_chat(chat_id: str):
    """Export chat history as PDF"""
    try:
        pdf_bytes = await chat_service.export_conversation(chat_id)
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=chat_{chat_id}.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
