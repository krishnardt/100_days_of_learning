from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import time, json, os
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse, Response
from starlette.requests import Request
from fastapi.responses import FileResponse
import qrcode
from io import BytesIO
from PIL import Image
import base64
import io, os
from starlette.responses import StreamingResponse


import pyqrcode
from pyqrcode import QRCode
import png


# Initialize the ArangoDB client.



app = FastAPI()
items = {}
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)
app.debug = True


image_path = 'C://Users/krish/Pictures/Screenshots/Screenshot.png'
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


template_dir = os.path.abspath(os.path.dirname(__file__))

# Now join the path to the actual template containing folder
# template_dir = os.path.join(template_dir, "pushers")
# template_dir = os.path.join(template_dir, "pushers_ng")

print(template_dir)
# Initialize templates variable by defining the containing directory
templates = Jinja2Templates(directory=template_dir)

print(templates)
print(templates.__dict__)
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))



@app.get('/')
async def get(request: Request):
	return FileResponse(image_path)



@app.get('/displayQR')
async def getQR(request:Request):
	# image = BytesIO()
	data = {'name':'krishna', 'age':26}
	qr.add_data(data)
	qr.make(fit=True)
	dest = os.path.dirname(os.path.realpath(__file__))
	img = qr.make_image(fill_color='black',black_color='white')
	final_path =dest+'\\'+data['name']+'.jpg'
	img.save(final_path)
	data['qrcode'] = final_path
	print(data) 

	#return FileResponse(final_path)
	return templates.TemplateResponse('testing.html',{"request": request, "details": data})

	#return Response(encoded_img)#{'image':url}#StreamingResponse(io.BytesIO(img.tobytes()), media_type="image/png")



if __name__=='__main__':    
    uvicorn.run(app, host='127.0.0.1', port=8000)







