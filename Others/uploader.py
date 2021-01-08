from typing import List

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="")



@app.get('/')
async def html_page(request: Request): 
	return templates.TemplateResponse("form.html", {'request': request})


@app.post("/upload")
async def main(request: Request, xmlFile: List[bytes] = File(...), typesystemFile: List[bytes] = File(...)):
	print(request.body())
	print(request.form())

	# file_like = open(video_path, mode="rb")
	# return StreamingResponse(file_like, media_type="video/mp4")
	return {"filenames": [f.filename for f in file]}