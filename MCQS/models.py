from .database import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 

class mcqs(base):
    __tablename__ = "mcqs"
    
    id = Column(Integer, primary_key= True, index = True)
    question = Column(String)
    answer = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("users", back_populates = 'mcq')


class users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index = True)
    email = Column(String)
    name = Column(String)
    password = Column(String)

    mcq = relationship('mcqs', back_populates= 'creator')