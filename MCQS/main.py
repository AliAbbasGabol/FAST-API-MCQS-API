
from fastapi import FastAPI
from MCQS import models
from MCQS.database import engine
from MCQS.routers import mcq, user, authentication
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

try:
    models.base.metadata.create_all(engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")


app.include_router(mcq.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
