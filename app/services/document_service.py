from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List, Optional
import tempfile
import os

class DocumentProcessor:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
    async def process_document(self, file: UploadFile) -> str:
        """Process uploaded document and create vectorstore"""
        if file.size > 15 * 1024 * 1024:  # 15MB limit
            raise ValueError("File size exceeds 15MB limit")

        temp_file_path = await self._save_temp_file(file)
        try:
            texts = await self._extract_text(temp_file_path, file.filename)
            vectorstore = await self._create_vectorstore(texts)
            return vectorstore
        finally:
            os.unlink(temp_file_path)

    async def _save_temp_file(self, file: UploadFile) -> str:
        """Save uploaded file to temporary location"""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            content = await file.read()
            temp_file.write(content)
            return temp_file.name
