import google.generativeai as genai
from typing import List, Optional
from app.models.chat import ChatMessage
from app.services.web_search import WebSearchTool

class ChatService:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.search_tool = WebSearchTool(max_results=3)

    async def get_response(
        self,
        message: str,
        conversation_history: List[ChatMessage],
        vectorstore_id: Optional[str] = None
    ) -> str:
        """Generate response using Gemini API"""
        context = self._build_context(message, conversation_history)
        search_results = await self._get_search_results(message)
        
        if vectorstore_id:
            doc_context = await self._get_document_context(vectorstore_id, message)
            context = f"{context}\n{search_results}\n{doc_context}"
        
        try:
            response = await self.model.generate_content(context)
            return response.text
        except Exception as e:
            raise Exception(f"Failed to generate response: {str(e)}")
