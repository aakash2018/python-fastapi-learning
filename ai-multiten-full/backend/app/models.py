from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime

class Tenant(BaseModel):
    id: str = Field(..., alias="tenant_id")
    name: Optional[str]

class User(BaseModel):
    id: str = Field(..., alias="user_id")
    tenant_id: str
    username: Optional[str]

class ChatMessage(BaseModel):
    id: Optional[str]
    tenant_id: str
    session_id: str
    user_id: str
    role: str
    content: Any
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ChatSession(BaseModel):
    id: Optional[str]
    tenant_id: str
    user_id: str
    use_case_id: Optional[str]
    metadata: Optional[dict] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UseCase(BaseModel):
    id: str
    tenant_id: str
    name: str
    description: Optional[str]
