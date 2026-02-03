
from pydantic import BaseModel


class MCQS(BaseModel):
    question: str
    answer: str

