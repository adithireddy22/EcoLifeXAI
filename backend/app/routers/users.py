from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError

from app.database import db
from app.schemas.user import UserCreate, UserUpdate, UserResponse


router = APIRouter(prefix="/api/users", tags=["Users"])

users_collection = db["users"]


def serialize_user(user: dict) -> dict:
    """Convert a MongoDB user document into an API response."""
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "sustainability_preferences": user.get(
            "sustainability_preferences", []
        ),
        "dietary_preferences": user.get(
            "dietary_preferences", []
        ),
    }


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_data: UserCreate):
    """Create a new user profile."""
    user_document = user_data.model_dump()
    user_document["created_at"] = datetime.now(timezone.utc)

    try:
        result = users_collection.insert_one(user_document)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )

    created_user = users_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_user(created_user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    """Retrieve a user by MongoDB ID."""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return serialize_user(user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user_data: UserUpdate):
    """Update a user's name or preferences."""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    updates = user_data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide at least one field to update.",
        )

    user = users_collection.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": updates},
        return_document=True,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return serialize_user(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    """Delete a user profile."""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )

    result = users_collection.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return None