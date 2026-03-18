from fastapi import FastAPI, UploadFile, File
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "CVisor Backend Running 🚀"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Read file
        file_bytes = await file.read()

        # Extract text
        extracted_text = extract_text_from_pdf(file_bytes)

        return {
            "filename": file.filename,
            "text_preview": extracted_text[:500],  # preview only
            "length": len(extracted_text)
        }

    except Exception as e:
        return {"error": str(e)}