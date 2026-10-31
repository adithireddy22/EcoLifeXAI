from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr

    sustainability_preferences: list[str] = Field(
        default_factory=list
    )

    dietary_preferences: list[str] = Field(
        default_factory=list
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )