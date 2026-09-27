from pydantic import BaseModel
from typing import Optional

class DocumentRequest(BaseModel):
    document_type: str = "NDA"
    party_name: str = "lavanya S"
    user_prompt: Optional[str] = "I need NDA"
    requirement: Optional[str] = None
    prompt: Optional[str] = None
    description: Optional[str] = None
    details: Optional[str] = None

class DocumentResponse(BaseModel):
    document: str
    document_type: str = "NDA"
    message: str = "Success"