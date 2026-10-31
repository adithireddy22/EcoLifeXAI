from datetime import datetime

from pydantic import BaseModel, Field


class SustainabilityReportCreate(BaseModel):
    user_id: str

    carbon_footprint_kg: float = Field(..., ge=0)
    water_usage_liters: float = Field(..., ge=0)
    energy_usage_kwh: float = Field(..., ge=0)

    recommendations: list[str] = Field(
        default_factory=list
    )

    explanation: str = ""


class SustainabilityReportResponse(SustainabilityReportCreate):
    id: str
    created_at: datetime