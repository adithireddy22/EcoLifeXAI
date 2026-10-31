from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    sustainability_preferences: list[str] = Field(default_factory=list)
    dietary_preferences: list[str] = Field(default_factory=list)


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    sustainability_preferences: list[str] | None = None
    dietary_preferences: list[str] | None = None


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    sustainability_preferences: list[str] = Field(default_factory=list)
    dietary_preferences: list[str] = Field(default_factory=list)