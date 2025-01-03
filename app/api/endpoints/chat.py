from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.chat import ChatMessage, ChatResponse
from app.services.chat_service import ChatService
from app.core.dependencies import get_chat_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def create_chat(
    message: ChatMessage,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Process a chat message and return response
    """
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
