from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from app.core.limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from app.api import (
    auth_router, vault_router, journal_router,
    calendar_router, file_router, email_router,
    todo_router, reminder_router
)

app = FastAPI(
    title="BuddyX API",
    description="Secure backend API for the BuddyX personal assistant app.",
    version="1.0.0"
)

# CORS configuration (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Register API routes
app.include_router(auth_router)
app.include_router(vault_router)
app.include_router(journal_router)
app.include_router(calendar_router)
app.include_router(file_router)
app.include_router(email_router)
app.include_router(todo_router)
app.include_router(reminder_router)

# Health check route
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the BuddyX Backend"}
