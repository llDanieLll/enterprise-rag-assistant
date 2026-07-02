from fastapi import FastAPI,UploadFile, File # type: ignore
from pathlib import Path 
app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    destination = UPLOAD_DIR / file.filename
    with open(destination, "wb") as buffer:
        buffer.write(await file.read())
    
    return{
        "filename":file.filename,
        "status": "uploaded"
    }    

@app.get("/")
def root():
    return{
        "message": "Enterprise RAG Assistant Backend"
    }