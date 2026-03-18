from pdfminer.high_level import extract_text
import tempfile
import os


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract text from PDF file bytes.

    Args:
        file_bytes (bytes): Uploaded PDF file content

    Returns:
        str: Extracted text
    """

    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file_bytes)
            temp_path = temp_file.name

        # Extract text
        text = extract_text(temp_path)

        # Cleanup temp file
        os.remove(temp_path)

        return text.strip()

    except Exception as e:
        print(f"[ERROR] PDF Parsing Failed: {e}")
        return ""