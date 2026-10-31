from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from app.database import db
from app.schemas.sustainability_report import (
    SustainabilityReportCreate,
    SustainabilityReportResponse,
)


router = APIRouter(prefix="/api/reports", tags=["Sustainability Reports"])

reports_collection = db["sustainability_reports"]
users_collection = db["users"]


def serialize_report(report: dict) -> dict:
    """Convert a MongoDB report document into an API response."""
    return {
        "id": str(report["_id"]),
        "user_id": report["user_id"],
        "carbon_footprint_kg": report["carbon_footprint_kg"],
        "water_usage_liters": report["water_usage_liters"],
        "energy_usage_kwh": report["energy_usage_kwh"],
        "recommendations": report.get("recommendations", []),
        "explanation": report.get("explanation", ""),
        "created_at": report["created_at"],
    }


@router.post(
    "",
    response_model=SustainabilityReportResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_report(report_data: SustainabilityReportCreate):
    """Create a sustainability report for an existing user."""
    if not ObjectId.is_valid(report_data.user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    user_exists = users_collection.find_one(
        {"_id": ObjectId(report_data.user_id)},
        {"_id": 1},
    )

    if user_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found. Create a user before adding a report.",
        )

    report_document = report_data.model_dump()
    report_document["created_at"] = datetime.now(timezone.utc)

    result = reports_collection.insert_one(report_document)

    created_report = reports_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_report(created_report)


@router.get(
    "/user/{user_id}",
    response_model=list[SustainabilityReportResponse],
)
def get_user_reports(user_id: str):
    """Retrieve all sustainability reports belonging to a user."""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    reports = reports_collection.find(
        {"user_id": user_id}
    ).sort("created_at", -1)

    return [serialize_report(report) for report in reports]


@router.get(
    "/{report_id}",
    response_model=SustainabilityReportResponse,
)
def get_report(report_id: str):
    """Retrieve a sustainability report by its ID."""
    if not ObjectId.is_valid(report_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid report ID.",
        )

    report = reports_collection.find_one(
        {"_id": ObjectId(report_id)}
    )

    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found.",
        )

    return serialize_report(report)


@router.delete(
    "/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_report(report_id: str):
    """Delete a sustainability report by its ID."""
    if not ObjectId.is_valid(report_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid report ID.",
        )

    result = reports_collection.delete_one(
        {"_id": ObjectId(report_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found.",
        )

    return None