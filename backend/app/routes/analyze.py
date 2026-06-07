from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.schemas import AnalyzeFileResponse
from app.services.analyzer_service import analyze_resume_text
from app.services.file_parser import extract_text_from_file
from app.services.job_matcher import calculate_job_match

router = APIRouter()


@router.post("/analyze-file", response_model=AnalyzeFileResponse)
async def analyze_file(
    file: UploadFile = File(...),
    job_description: str | None = Form(None)
):
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

    response = {
        "filename": file.filename,
        "extracted_text_preview": text[:1000],
        "analysis": analysis
    }

    if job_description and job_description.strip():
        match_result = calculate_job_match(text, job_description)

        response.update(match_result)

    return response