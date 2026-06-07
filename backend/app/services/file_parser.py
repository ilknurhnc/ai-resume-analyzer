from io import BytesIO

from docx import Document
from pypdf import PdfReader


PDF_CONTENT_TYPE = "application/pdf"
DOCX_CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


def clean_extracted_text(text: str) -> str:
    text = text.replace("\x7f", " ")
    text = text.replace("\uFFFD", " ")

    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    return "\n".join(lines)


def extract_text_from_pdf(file_content: bytes) -> str:
    pdf = PdfReader(BytesIO(file_content))

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return clean_extracted_text(text)


def extract_text_from_docx(file_content: bytes) -> str:
    document = Document(BytesIO(file_content))

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())

    text = "\n".join(paragraphs)

    return clean_extracted_text(text)


def extract_text_from_file(file_content: bytes, content_type: str) -> str:
    if content_type == PDF_CONTENT_TYPE:
        return extract_text_from_pdf(file_content)

    if content_type == DOCX_CONTENT_TYPE:
        return extract_text_from_docx(file_content)

    raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")