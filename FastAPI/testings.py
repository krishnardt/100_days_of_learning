from fastapi.testclient import TestClient
from fastapi import FastAPI
from fastapi.websockets import WebSocket

app = FastAPI()


@app.websocket("/ws/{x}/something")
async def websocket(websocket: WebSocket, x: str):
	await websocket.accept()
	await websocket.send_json({"msg": "Hello WebSocket"})
	await websocket.close()






def test_websocket():
	client = TestClient(app)
    
    with client.websocket_connect("/ws/this/something") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}


test_websocket()
