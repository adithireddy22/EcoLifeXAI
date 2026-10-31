from datetime import datetime, timezone

from pydantic import BaseModel, Field


class ChatHistoryModel(BaseModel):
    user_id: str
    session_id: str

    message: str = Field(..., min_length=1)
    response: str = Field(..., min_length=1)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )