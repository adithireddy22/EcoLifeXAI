from datetime import datetime, timezone

from pydantic import BaseModel, Field


class ShoppingAnalysisModel(BaseModel):
    user_id: str
    product_name: str

    barcode: str | None = None

    nutrition_score: float | None = Field(
        default=None, ge=0, le=100
    )

    environmental_score: float | None = Field(
        default=None, ge=0, le=100
    )

    ingredients: list[str] = Field(
        default_factory=list
    )

    recommendations: list[str] = Field(
        default_factory=list
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )