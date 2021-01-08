# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:36:18 2020

@author: krish
"""

"""
case when you want your websocket server has to be a listener

"""

from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
from starlette.middleware.cors import CORSMiddleware
import uvicorn
#from fastapi.responses import HTMLResponse

app=FastAPI()


#adding middle ware facilitates us to open/run api from any device connected to a LAN that a server is connected
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)
app.debug = True



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive()
            print(data)
            await websocket.send_text(f"{data}")
        except WebSocketDisconnect:
            print("radom")
            await websocket.close()


if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000)
