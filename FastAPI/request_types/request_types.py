# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:17:38 2020

@author: krish
"""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder



app = FastAPI()



@app.post('/check')
async def check(request: Request):
    da = await request.form()
    da = jsonable_encoder(da)
    print(da)
    return da