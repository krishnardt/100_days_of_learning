from fastapi import FastAPI, BackgroundTasks, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse



# app = FastAPI()


# def testing():
# 	print("we are testing background task")
# 	return True



# @app.get("/")
# async def user(error:bool):
#     #background_tasks.add_task(testing)
#     #raise HTTPException(status_code=200, detail="example error")
#     return JSONResponse(status_code=200)




from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_video_streamer():
    for i in range(100000):
        yield b"some fake video bytes\n"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())