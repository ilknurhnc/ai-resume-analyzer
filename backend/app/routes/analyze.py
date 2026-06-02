from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas import AnalyzeFileResponse
from app.services.analyzer_service import analyze_resume_text
from app.services.file_parser import extract_text_from_file

router = APIRouter()


@router.post("/analyze-file", response_model=AnalyzeFileResponse)
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()

    try:
        text = extract_text_from_file(content, file.content_type)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the uploaded file."
        )

    analysis = analyze_resume_text(text)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "extracted_text_preview": text[:1000],
        "analysis": analysis
    }