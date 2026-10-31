import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

# Load .env from the backend root
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_FILE)

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv(
    "MONGODB_DATABASE", "ecolifexai"
)

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is missing from backend/.env")

# MongoDB connection
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

db = client[MONGODB_DATABASE]


def check_mongodb_connection():
    """Verify connectivity to MongoDB."""
    client.admin.command("ping")
    return True


# Collections required by EcoLifeXAI
COLLECTION_NAMES = [
    "users",
    "sustainability_reports",
    "shopping_analyses",
    "chat_history",
]


def initialize_collections():
    """Create required collections if they do not exist."""

    existing_collections = set(db.list_collection_names())

    for collection_name in COLLECTION_NAMES:
        if collection_name in existing_collections:
            print(f"Collection already exists: {collection_name}")
            continue

        try:
            db.create_collection(collection_name)
            print(f"Created collection: {collection_name}")

        except CollectionInvalid:
            # Another process may have created it concurrently.
            print(f"Collection already exists: {collection_name}")


def create_indexes():
    """Create indexes for frequently queried fields."""

    # Ensure that every user has a unique email address.
    db["users"].create_index(
        [("email", 1)],
        unique=True,
        name="unique_user_email"
    )

    # Retrieve a user's sustainability reports by newest first.
    db["sustainability_reports"].create_index(
        [
            ("user_id", 1),
            ("created_at", -1)
        ],
        name="user_reports_by_date"
    )

    # Retrieve a user's shopping analyses by newest first.
    db["shopping_analyses"].create_index(
        [
            ("user_id", 1),
            ("created_at", -1)
        ],
        name="user_shopping_by_date"
    )

    # Retrieve messages from a conversation chronologically.
    db["chat_history"].create_index(
        [
            ("user_id", 1),
            ("session_id", 1),
            ("created_at", 1)
        ],
        name="user_chat_session_by_date"
    )

    print("EcoLifeXAI indexes created successfully.")
