from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.document_service import DocumentProcessor
from app.core.dependencies import get_document_processor

router = APIRouter()

@router.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    document_processor: DocumentProcessor = Depends(get_document_processor)
):
    """
    Upload and process a document
    """
    try:
        vectorstore = await document_processor.process_document(file)
        return {"message": "Document processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
