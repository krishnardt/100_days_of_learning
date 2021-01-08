# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:36:18 2020

@author: krish
"""

"""
case when you want your websocket server has to be a listener

"""

from fastapi import FastAPI, WebSocket
from starlette.middleware.cors import CORSMiddleware
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
        data = await websocket.receive_text()
        print(data)


