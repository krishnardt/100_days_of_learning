from fastapi import FastAPI, File, UploadFile, Header, Depends, HTTPException, status
import uvicorn
from typing import List
from fastapi.responses import HTMLResponse
from pathlib import Path
from tempfile import NamedTemporaryFile
import tempfile
import shutil, os
from pydantic import BaseModel, EmailStr




app = FastAPI()


class FilePath(BaseModel):
	path : str



async def valid_content_length(content_length: int = Header(..., lt=500)):
    return content_length



@app.post("/files")
async def create_files(files: List[bytes] = File(...), file_size: int = Depends(valid_content_length)):
    return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...), file_size: int = Depends(valid_content_length)):
#     # return {"filenames": {file.filename:[file.filename,Path(file.filename).suffix, tempfile.mkstemp(prefix='parser_', suffix=extension)[1], file.content_type] for file in files}}
#     file_details = {}
#     real_file_size = 0
#     temp: IO = NamedTemporaryFile(delete=False)
#     dest_path = "E://100_days_of_learning/"

#     size_overflow = False
#     for file in files:
#     	for chunk in file.file:
#     		real_file_size += len(chunk)
#     		if real_file_size >= file_size:
#     			size_overflow = True
#     			break;
    			

#     if size_overflow == True:
#     	raise HTTPException(
#                 	status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Too large"
#             	)
#     else:
# 	    for file in files:
# 	    	extension = Path(file.filename).suffix
# 	    	_, path = tempfile.mkstemp(prefix='parser_', suffix=extension)
# 	    	file_details[file.filename] = [extension, path, file.content_type]
# 	    	with open(os.path.join(dest_path, file.filename), 'wb+') as folder:
# 	    		shutil.copyfileobj(file.file, folder)

#     return file_details



@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):#, file_size: int = Depends(valid_content_length)):
    # return {"filenames": {file.filename:[file.filename,Path(file.filename).suffix, tempfile.mkstemp(prefix='parser_', suffix=extension)[1], file.content_type] for file in files}}
    """
    parameters:
    file_size: checking the size for all files..
    files: multiple files
    @return:
    if fails due to overall upload file size increases, it throws the exception with the type of file it has issue.
    if succeeds, copies the file to the destination folder.

    """
    file_details = {}
    file_size = 100000
    
    #temp: IO = NamedTemporaryFile(delete=False)
    dest_path = "E://100_days_of_learning/"
    real_file_size = 0
    size_overflow = False
    overflown_format = ''
    for file in files:
    	extension = Path(file.filename).suffix
    	print(file.filename)
    	for chunk in file.file:
    		real_file_size += len(chunk)
    		if real_file_size >= file_size:
    			size_overflow = True
    			overflown_format = extension
    			break;
    			

    if size_overflow == True:
    	raise HTTPException(
                	status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="{} is Too large".format(overflown_format)
            	)
    else:
	    for file in files:
	    	#temp: IO = NamedTemporaryFile(delete=False)
	    	extension = Path(file.filename).suffix
	    	_, path = tempfile.mkstemp(prefix='parser_', suffix=extension)
	    	file_details[file.filename] = [extension, path, file.content_type]
	    	with open(os.path.join(dest_path, file.filename), 'wb+') as folder:
	    		shutil.copyfileobj(file.file, folder)

    return file_details





@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)