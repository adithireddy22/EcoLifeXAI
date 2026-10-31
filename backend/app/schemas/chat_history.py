from datetime import datetime

from pydantic import BaseModel, Field


class ChatMessageCreate(BaseModel):
    user_id: str = Field(..., min_length=1)
    session_id: str = Field(..., min_length=1, max_length=100)
    role: str = Field(..., pattern="^(user|assistant)$")
    message: str = Field(..., min_length=1, max_length=10000)


class ChatMessageResponse(BaseModel):
    id: str
    user_id: str
    session_id: str
    role: str
    message: str
    created_at: datetime