from io import BytesIO
from pypdf import PdfReader


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