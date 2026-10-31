from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from app.database import check_mongodb_connection

from app.core.config import APP_NAME, APP_ENV, DEBUG

from app.routers.users import router as users_router
from app.routers.reports import router as reports_router
from app.routers.shopping import router as shopping_router
from app.routers.chat import router as chat_router


# Create the FastAPI application
app = FastAPI(
    title=APP_NAME,
    description=(
        "Backend API for sustainable living "
        "and personalized well-being."
    ),
    version="1.0.0",
    debug=DEBUG,
)

app.include_router(users_router)
app.include_router(reports_router)
app.include_router(shopping_router)
app.include_router(chat_router)

# Configure CORS for local React development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to EcoLifeXAI",
        "environment": APP_ENV,
    }


# Health-check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": APP_NAME,
    }

@app.get("/db-health")
def database_health():
    try:
        check_mongodb_connection()
        return {
            "status": "success",
            "database": "connected"
        }
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed. Check Atlas configuration."
        )