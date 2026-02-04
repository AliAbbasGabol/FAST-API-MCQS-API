from fastapi import APIRouter, Depends, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..Repository import user


router = APIRouter(tags=['user'],prefix="/user")

get_db = database.get_db



@router.post("/",response_model=schemas.show_user)
def user_reqister(request: schemas.user, db : Session = Depends(get_db)):
    return user.create_user(request, db)
    


@router.get("/{id}", response_model=schemas.show_user)
def users_get(id: int, db : Session = Depends(get_db)):
    return user.get_user(id,db)