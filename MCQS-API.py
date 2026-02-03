from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def inedx():
    return {"data": {"message":"hey"}}

@app.get("/mcqs")
def mcqs(limit=3, sort: Optional[str]= "desecnding"):
    return {"data": f'total mcqs given = {limit}'}


@app.get("/mcqs/{id}")
def mcq(id: int):
    return {"data": id}

class MCQS(BaseModel):
    title: str
    name: str
    number: Optional[int]

@app.post("/mcqs")
def new_mcqs(request: MCQS):
    return request
    return {"data": {"mcq1": "why"}}