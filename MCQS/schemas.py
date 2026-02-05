
from pydantic import BaseModel
from typing import Optional, List

class user(BaseModel):
    name: str
    email: str
    password: str


class MCQS(BaseModel):
    question: str
    answer: str

class show_user(BaseModel):
    name: str
    email: str
    mcq: List[MCQS]=[]
    class Config():
        orm_model = True



class show_mcqs(BaseModel):
    question: str
    answer: str
    creator: Optional[show_user] = None
    class Config():
        orm_model = True


class login(BaseModel):
    email: str
    passowrd: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None