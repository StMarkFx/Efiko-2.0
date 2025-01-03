from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Document(BaseModel):
    id: str
    filename: str
    vectorstore_id: str
    created_at: datetime
    updated_at: datetime
    file_size: int
    file_type: str
    processed: bool
    error: Optional[str] = None
