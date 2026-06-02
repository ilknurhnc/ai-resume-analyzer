from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0.0"
)

app.include_router(analyze_router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "AI Resume Analyzer API is running"
    }
