# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:04:17 2020

@author: krish
"""

from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
from websocket import create_connection
import pika
import uvicorn
from websockets_trial import manager, app
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from arango import ArangoClient
import time, json
from typing import List
from starlette.middleware.cors import CORSMiddleware
# Initialize the ArangoDB client.



#app = FastAPI()

items = {}
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)
app.debug = True


#@app.on_event("startup")
#async def startup_event():
#    items["foo"] = {"name": "Fighters"}
#    items["bar"] = {"name": "Tenders"}
#    print(items)
#    
#    connection = pika.BlockingConnection(
#    pika.ConnectionParameters(host='localhost'))
#    channel = connection.channel()
#
#
#@app.get("/items/{item_id}")
#async def read_items(item_id: str):
#    return items[item_id]
#
#
#@app.on_event("shutdown")
#async def end_events():
#    connection.close()
    
    
#if eva.db_conn.has_graph('school'):
#    school = eva.db_conn.graph('school')
#else:
#    school = eva.db_conn.create_graph('school')
#
#
#if school.has_vertex_collection('teachers'):
#    teachers = school.vertex_collection('teachers')
#else:
#    teachers = school.create_vertex_collection('teachers')

def callback(ch, method, properties, body):
    print(ch)
    print(method)
    print(properties)
    #print(dict(properties))
    print(" [x] Received %r" % body)


    

class EventsLookUp:
    
    def __init__(self, host):
#        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#        self.channel = self.connection.channel()
        self.host = host
        self.connection = ''
        self.websocket_manager = ''
        self.db_client = ''
        self.db_conn = ''
    

eva = EventsLookUp('127.0.0.1')

@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
    print(items)
    
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=eva.host))
    eva.channel = connection.channel()
    eva.channel.exchange_declare(exchange='notifications', exchange_type='direct')
    eva.channel.exchange_declare(exchange='actions', exchange_type='direct')
    eva.channel.exchange_declare(exchange='Actions', exchange_type='fanout')
    eva.channel.queue_declare(queue='hello2', durable=True)
    eva.channel.queue_declare(queue='hello3', durable=True)
    eva.channel.queue_declare(queue='actions1', durable=True)
    eva.channel.queue_declare(queue='actions2', durable=True)
    print(eva.channel)
    eva.websocket_manager = manager
    eva.db_client = ArangoClient()
    # Connect to "test" database as root user.
    eva.db_conn = eva.db_client.db('_system', username='root', password='arangodb')



@app.on_event("shutdown")
async def end_events():
    print("connection is being ended")
    eva.connection.close()


class User(BaseModel):
    id: int
    name: str
    joined: str


#def websocket_client(data):
#    print("entering into client web socket")
#    print(data)
#    conn = create_connection("ws://localhost:8000/ws")
#    print(conn)
#    try:
#        #time.sleep(1)
#        print("sending data from client to server listener")
#        di = str({'a':'b'})
#        print(di)
#        d = json.dumps(di)
#        print(d)
#        conn.send(d)
#        res = conn.recv();
#        print(res)
#        #print("data sent...")
#        #time.sleep(1)
#        conn.close()
#    except:
#        conn.close()

def create_n_notifications(details):
    users = details['invitees']
    detail = details['data']
    notifications = {}
    for user in users:
        notifications[user] = detail
    
    return notifications



@app.post("/adding")
async def adding(user: User):
    users = jsonable_encoder(user)
#    if eva.db_conn.has_graph('school'):
#        school = eva.db_conn.graph('school')
#    else:
#        school = eva.db_conn.create_graph('school')
#
#
#    if school.has_vertex_collection('teachers'):
#        teachers = school.vertex_collection('teachers')
#    else:
#        teachers = school.create_vertex_collection('teachers')
#    
#    result = teachers.insert(users)
#    print(result)
    
    details = {
            "invitees" : ['krishna', 'mohan', 'injeti'],
            "data":'we have meeting at 10 a.m.'
            }
    notifications = create_n_notifications(details)
    for k, v in notifications.items():
        eva.channel.basic_publish(exchange='notifications', routing_key='hello2', body=k+" has "+v)
    


class Actions_(BaseModel):
    invitees: List
    data: str#"complete rabbit mq today"
    #status:"not yet done"

@app.post('/insert_actions')
async def actions(action: Actions_):
    users = dict(action)
    
    #detail = users['desc']
    #names = users['names']
    print(users)
    print(type(users))
    notifications = create_n_notifications(users)
    print(notifications)
    for k, v in notifications.items():
        eva.channel.basic_publish(exchange='Actions', routing_key='', body=k+" has "+v)
        
    
    
    
    



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print(" entered into websocket server")
    await eva.websocket_manager.connect(websocket)
    print("websocket connected")
    try:
        while True:
            print(websocket)
            data = await websocket.receive_text()
            print(data)
            await eva.websocket_manager.send_personal_message("You wrote: "+str(data), websocket)
            #await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        eva.websocket_manager.disconnect(websocket)
        #await manager.broadcast(f"Client left the chat")



@app.websocket("/ws1")
async def websocket_endpoint(websocket: WebSocket):
    print(" entered into websocket server1")
    await eva.websocket_manager.connect(websocket)
    print("websocket1 connected")
    try:
        while True:
            print(websocket)
            data = await websocket.receive_text()
            print(data)
            await eva.websocket_manager.send_personal_message("You wrote: "+str(data), websocket)
            #await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        eva.websocket_manager.disconnect(websocket)
        #await manager.broadcast(f"Client left the chat")
    
        
    


if __name__=='__main__':
    
    uvicorn.run(app, host='127.0.0.1', port=8000)
    