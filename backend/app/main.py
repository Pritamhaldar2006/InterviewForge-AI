from fastapi import FastAPI

from app.api.sessions import router as sessions_router

app = FastAPI(
    title="AI Interview Simulator",
    description="AI-powered technical interview simulator",
    version="1.0.0",
)

app.include_router(
    sessions_router
)

@app.get("/")
def root():
    return {
        "message": "AI Interview Simulator API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }