from datetime import datetime, timezone

from pydantic import BaseModel, Field


class SustainabilityReportModel(BaseModel):
    user_id: str

    carbon_footprint_kg: float = Field(..., ge=0)
    water_usage_liters: float = Field(..., ge=0)
    energy_usage_kwh: float = Field(..., ge=0)

    recommendations: list[str] = Field(
        default_factory=list
    )

    explanation: str = ""

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )