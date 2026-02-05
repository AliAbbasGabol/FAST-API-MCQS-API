
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Use environment variable if available, otherwise default to local sqlite
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./mcqs.db')


connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)


base = declarative_base()


session_local = sessionmaker(bind=engine, autocommit = False, autoflush= False)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()