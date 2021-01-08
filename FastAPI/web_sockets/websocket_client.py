# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:37:01 2020

@author: krish
"""

#from fastapi import FastAPI, WebSocket
#from starlette.middleware.cors import CORSMiddleware
from websocket import create_connection
import time
import json
#import uvicorn
#from fastapi.responses import HTMLResponse

#app=FastAPI()
#
#
##adding middle ware facilitates us to open/run api from any device connected to a LAN that a server is connected
#app.add_middleware(
#    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
#)
#app.debug = True
conn = create_connection("ws://localhost:8000/ws")
try:
    time.sleep(1)
    print("sending data from client to server listener")
    di = str({'a':'b'})
    print(di)
    d = json.dumps(di)
    print(d)
    conn.send(d)
    res = conn.recv();
    print(res)
    #print("data sent...")
    #time.sleep(1)
    conn.close()
except:
    conn.close()
    
    
conn = create_connection("ws://localhost:8000/ws1")
try:
    time.sleep(1)
    print("sending data from client to server listener1")
    di = str({'a':'b'})
    print(di)
    d = json.dumps(di)
    print(d)
    conn.send(d)
    res = conn.recv();
    print(res)
    #print("data sent...")
    #time.sleep(1)
    conn.close()
except:
    conn.close()
