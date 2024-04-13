from fastapi import FastAPI, Response
import json
from random import *
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


fakeResponse = {
    "field1": "str",
    "field2": True,
    "field3": 123,
    "field4": 3.14,
    "field5": "2023-07-07T17:55:27.958Z",
    "field6": ["str", "str", "str"],
}


class RequestModel(BaseModel):
    field1: Optional[str] = Field(
        default='str',
        title='Поле 1',
        description='Описание',
        max_length=30)
    field2: bool
    field3: int
    field4: float
    field5: datetime
    field6: List[str]


class ResponseModel(BaseModel):
    field1: bool
    field2: str
    field3: int
    field4: float
    field5: datetime
    field6: List[str]


class ErrorModel(BaseModel):
    error: str

def _proxy(*args, **kwargs):
    t_resp = requests.request(
        method="GET",
        url='http://fastapi-server:20001/',
        allow_redirects=False)

    response = Response(content=t_resp.content, status_code=t_resp.status_code)
    return response

@app.get("/test-proxy")
async def proxy():
    return _proxy()



