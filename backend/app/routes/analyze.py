from fastapi import APIRouter, UploadFile, File

from app.services.file_parser import extract_text_from_pdf
from app.services.analyzer_service import analyze_resume_text

router = APIRouter()


@router.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()

    text = extract_text_from_pdf(content)
    analysis = analyze_resume_text(text)

    return {
        "filename": file.filename,
        "extracted_text_preview": text[:1000],
        "analysis": analysis
    }