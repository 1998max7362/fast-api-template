from fastapi import FastAPI, Depends
import json
from random import *
from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/examp", response_model=ResponseModel)
async def answerDevices():
    return fakeResponse


@app.post("/examp", responses={201: {"model": ResponseModel}, 400: {"model": ErrorModel}})
async def postServers(req: RequestModel):
    return {"res": "ok", "req": req}


@app.put("/examp", responses={200: {"model": ResponseModel}, 400: {"model": ErrorModel}})
async def postServers(req: RequestModel):
    return {"res": "ok", "req": req}


@app.patch("/examp", responses={200: {"model": ResponseModel}, 400: {"model": ErrorModel}})
async def postServers(req: RequestModel):
    return {"res": "ok", "req": req}


@app.delete("/examp", responses={200: {"model": ResponseModel}, 400: {"model": ErrorModel}})
async def postServers():
    return {"res": "ok"}


@app.get("/")
async def homepage():
    print('получил запрос')
    data = json.dumps({'hello': 'world'})
    return data


# --------------------
class Object1(BaseModel):
    prop1: str

class Object2(BaseModel):
    prop2: int

class Object3(BaseModel):
    prop3: float

# Define a union of the different object types
Object = Union[Object1, Object2, Object3]


data =  [
        {"prop1": "value1"},
        {"prop2": 123},
        {"prop3": 3.14}
    ]

@app.get("/dif_objects")
async def dif_objects()->List[Object]:
    return data

#  --------------------------------------------
class QueryModel(BaseModel):
   query_param1: str 


@app.get("/query_params")
async def dif_objects(model: QueryModel = Depends())->ResponseModel:
    return data

#  --------------------------------------------

@app.get("/liveness")
async def liveness()->None:
    return 

@app.get("/readness", responses={200: {}, 503: {}})
async def readness()->None:
    return 
