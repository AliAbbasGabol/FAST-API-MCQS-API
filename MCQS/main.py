
from fastapi import FastAPI
from MCQS import models
from MCQS.database import engine
from MCQS.routers import mcq, user, authentication


app = FastAPI()


models.base.metadata.create_all(engine)


app.include_router(mcq.router)
app.include_router(user.router)
app.include_router(authentication.router)
