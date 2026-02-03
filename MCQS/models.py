from .database import base
from sqlalchemy import Column, Integer, String

class mcqs(base):
    __tablename__ = "mcqs_1"
    
    id = Column(Integer, primary_key= True, index = True)
    question = Column(String)
    answer = Column(String)