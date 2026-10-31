from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from app.database import db
from app.schemas.chat_history import (
    ChatMessageCreate,
    ChatMessageResponse,
)

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat History"],
)

chat_collection = db["chat_history"]
users_collection = db["users"]


def serialize_message(document: dict) -> dict:
    return {
        "id": str(document["_id"]),
        "user_id": document["user_id"],
        "session_id": document["session_id"],
        "role": document["role"],
        "message": document["message"],
        "created_at": document["created_at"],
    }


def validate_user(user_id: str):
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


@router.post(
    "",
    response_model=ChatMessageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_chat_message(chat_data: ChatMessageCreate):
    validate_user(chat_data.user_id)

    document = chat_data.model_dump()
    document["created_at"] = datetime.now(timezone.utc)

    result = chat_collection.insert_one(document)

    saved_message = chat_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_message(saved_message)


@router.get(
    "/user/{user_id}",
    response_model=list[ChatMessageResponse],
)
def get_user_chat_history(user_id: str):
    validate_user(user_id)

    messages = chat_collection.find(
        {"user_id": user_id}
    ).sort("created_at", 1)

    return [
        serialize_message(message)
        for message in messages
    ]


@router.get(
    "/{user_id}/{session_id}",
    response_model=list[ChatMessageResponse],
)
def get_session_chat_history(
    user_id: str,
    session_id: str,
):
    validate_user(user_id)

    messages = chat_collection.find(
        {
            "user_id": user_id,
            "session_id": session_id,
        }
    ).sort("created_at", 1)

    return [
        serialize_message(message)
        for message in messages
    ]


@router.delete(
    "/{user_id}/{session_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_chat_session(
    user_id: str,
    session_id: str,
):
    validate_user(user_id)

    result = chat_collection.delete_many(
        {
            "user_id": user_id,
            "session_id": session_id,
        }
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No messages found for this chat session.",
        )

    return None