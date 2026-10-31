from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from app.database import db
from app.schemas.shopping_analysis import (
    ShoppingAnalysisCreate,
    ShoppingAnalysisResponse,
)

router = APIRouter(
    prefix="/api/shopping",
    tags=["Shopping Analysis"],
)

shopping_collection = db["shopping_analyses"]
users_collection = db["users"]


def serialize_analysis(analysis: dict) -> dict:
    return {
        "id": str(analysis["_id"]),
        "user_id": analysis["user_id"],
        "product_name": analysis["product_name"],
        "barcode": analysis.get("barcode"),
        "data_source": analysis.get("data_source", "manual"),
        "basis": analysis.get("basis", "per_100g"),
        "ingredients": analysis.get("ingredients", []),
        "nutrients": analysis.get("nutrients", {}),
        "nutrition_score": analysis.get("nutrition_score"),
        "environmental_score": analysis.get("environmental_score"),
        "recommendations": analysis.get("recommendations", []),
        "created_at": analysis["created_at"],
    }


@router.post(
    "",
    response_model=ShoppingAnalysisResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_shopping_analysis(
    analysis_data: ShoppingAnalysisCreate,
):
    # Validate the user ID format
    if not ObjectId.is_valid(analysis_data.user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    # Verify that the user exists
    user = users_collection.find_one(
        {"_id": ObjectId(analysis_data.user_id)},
        {"_id": 1},
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found. Create a user before adding a shopping analysis.",
        )

    # Prepare the document
    analysis_document = analysis_data.model_dump()
    analysis_document["created_at"] = datetime.now(timezone.utc)

    # Save to MongoDB
    result = shopping_collection.insert_one(analysis_document)

    # Retrieve the inserted document
    created_analysis = shopping_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_analysis(created_analysis)


@router.get(
    "/user/{user_id}",
    response_model=list[ShoppingAnalysisResponse],
)
def get_user_shopping_analyses(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    user = users_collection.find_one(
        {"_id": ObjectId(user_id)},
        {"_id": 1},
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    analyses = shopping_collection.find(
        {"user_id": user_id}
    ).sort("created_at", -1)

    return [
        serialize_analysis(analysis)
        for analysis in analyses
    ]


@router.get(
    "/{analysis_id}",
    response_model=ShoppingAnalysisResponse,
)
def get_shopping_analysis(analysis_id: str):
    if not ObjectId.is_valid(analysis_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid shopping analysis ID.",
        )

    analysis = shopping_collection.find_one(
        {"_id": ObjectId(analysis_id)}
    )

    if analysis is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shopping analysis not found.",
        )

    return serialize_analysis(analysis)


@router.delete(
    "/{analysis_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_shopping_analysis(analysis_id: str):
    if not ObjectId.is_valid(analysis_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid shopping analysis ID.",
        )

    result = shopping_collection.delete_one(
        {"_id": ObjectId(analysis_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shopping analysis not found.",
        )

    return None