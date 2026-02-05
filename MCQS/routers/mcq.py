from fastapi import APIRouter, Depends, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..Repository import mcq
from . import oauth2

router = APIRouter(tags=['mcqs'],prefix="/mcqs")

get_db = database.get_db

@router.get("/",response_model=list[schemas.show_mcqs])
def read(db : Session = Depends(get_db), get_current_user = Depends(oauth2.get_current_user)):
    return mcq.get_all(db)


@router.post("/", status_code = 201)
def create(request: schemas.MCQS, db : Session = Depends(get_db), get_current_user = Depends(oauth2.get_current_user)):
    return mcq.create_mcq(request, db)
    


@router.delete("/{id}")
def deletor(mcq_id: int, db : Session = Depends(get_db), get_current_user = Depends(oauth2.get_current_user)):
    return mcq.delete_mcq(mcq_id, db)
    
    


@router.put("/{id}",status_code = 202)
def updator(request: schemas.MCQS, mcq_id: int, db : Session = Depends(get_db), get_current_user = Depends(oauth2.get_current_user)):
    return mcq.update_mcq(request, mcq_id, db)


@router.get("/{id}",response_model=schemas.show_mcqs)
def reader(mcq_id: int, db: Session = Depends(get_db), get_current_user = Depends(oauth2.get_current_user)):
    return mcq.get_mcq(mcq_id, db)


