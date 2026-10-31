from app.database import (
    check_mongodb_connection,
    initialize_collections,
    create_indexes,
)


def main():
    print("Connecting to MongoDB...")

    try:
        check_mongodb_connection()
        print("MongoDB connected successfully!")

        print("\nInitializing collections...")
        initialize_collections()

        print("\nCreating indexes...")
        create_indexes()

        print("\nEcoLifeXAI database initialization completed!")

    except Exception as error:
        print(f"\nDatabase initialization failed: {error}")
        raise


if __name__ == "__main__":
    main()