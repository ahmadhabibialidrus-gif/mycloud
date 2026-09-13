from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
from pathlib import Path


app = FastAPI()


STORAGE_DIR = Path("../storage")
STORAGE_DIR.mkdir(exist_ok=True)



@app.get("/")
def home():
	return FileResponse("../frontend/index.html")


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
	file_path = STORAGE_DIR / file.filename


	with open(file_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)


	return {
		"message": "File berhasil diupload",
		"filename": file.filename
	}


@app.get("/files")
def list_files():
	files = []


	for file in STORAGE_DIR.iterdir():
		if file.is_file():
			files.append({
				"name": file.name,
				"size": file.stat().st_size
			})

	return files














































































