# import uvicorn
# from fastapi import Body, FastAPI

# app = FastAPI()


# @app.post("/test")
# async def update_item(
#         payload: str = Body(...)
# ):
# 	print(payload)
# 	return {"found........."}





# from fastapi import FastAPI
# from fastapi.websockets import WebSocket




# from fastapi import FastAPI
import uvicorn

# app = FastAPI()


# @app.get("/user/me")
# def read_user_me():
#    return {"Hello": "World2" }


# @app.get("/user/{user}")
# def read_user():
#     return {"Hello": "World"}






from typing import Dict
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, status
from pydantic import BaseModel

# def get_datastore() -> Dict:
#     return {1: {"type": "fsg", "info": "information"},
#                 2: {"type": "asg", "info": "information"},}

# app = FastAPI()




# class FSG(BaseModel):
# 	types: str


# @app.get("/fsgs", summary="Get all registered FSGs", operation_id="get_fsgs",)
# async def get_fsgs(fsg: FSG):
#     print(app.url_path_for(name="get_lsgs")+"?type="+fsg.types)
#     return RedirectResponse(url=app.url_path_for(name="get_lsgs")+"?type=fsg", status_code=status.HTTP_302_FOUND)#, query_params={"type": "fsg"})

# @app.get("/lsgs", summary="Get all registered LSGs", operation_id="get_lsgs", name="get_lsgs")
# async def get_lsgss(type: str):
#     glob= get_datastore()

#     lsgs = [lsg for lsg in glob.values() if lsg.get("type") == type]

#     return {"data": [lsg.get("info") for lsg in lsgs]}

# from typing import Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()


# @app.post("/items")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
from user_agents import parse
import platform as pf
from getmac import get_mac_address
from socket import gethostbyname, gethostname
import datetime


@app.get("/device_details")
async def logged_in(request:Request):
    #cuser = get_user(email)
    device = list(pf.uname())
    platform_keys = ['device_type', 'device_name', 'release', 'version', 'machine', 'processor']
    device_details =dict(zip(platform_keys, device)) 
    device_details['ip_address'] = gethostbyname(gethostname())
    device_details['mac_address'] = get_mac_address()
    #device_details['_key'] = email+'_'+device_details['device_name']
    device_details['login_time'] = str(datetime.datetime.now())
    #device_details["login_type"] = log_type
    user_agent = parse(request.headers["user-agent"])
    print(user_agent)
    device_details["browser"] = user_agent.browser.family+user_agent.browser.version_string
    print(device_details)
    print("\n\n\n\n")

    # if cuser:
    #     if login_devices.has(device_details['_key']):
    #         #login_devices.update({"_key":device_details['_key'],"device_name":device,"login_time":f"{datetime.datetime.now()}","login_type":log_type})
    #         login_devices.update(device_details)
    #     else:
    #         #login_devices.insert({"_key":device_details['_key'],"device_name":device,"login_time":f"{datetime.datetime.now()}","login_type":log_type})
    #         login_devices.insert(device_details)















# from datetime import datetime

# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# start = datetime.today()


# @app.get("/")
# async def root(start_date: datetime = start):
#     print(start_date)
#     return {"start_date": start_date}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# app = FastAPI()


# @app.websocket_route("/ws/{arg}/something")
# async def websocket(arg, websocket: WebSocket):
#     await websocket.accept()
#     await websocket.send_json({"msg": "Hello WebSocket"})
#     await websocket.close()


# def test_websocket():
#     client = TestClient(app)
#     with client.websocket_connect("/ws/this/something") as websocket:
#         data = websocket.receive_json()
#         assert data == {"msg": "Hello WebSocket"}

#test_websocket()

