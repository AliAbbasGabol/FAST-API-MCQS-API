from fastapi import APIRouter, Depends, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..Repository import mcq

router = APIRouter(tags=['mcqs'],prefix="/mcqs")

get_db = database.get_db

@router.get("/",response_model=list[schemas.show_mcqs])
def read(db : Session = Depends(get_db)):
    return mcq.get_all(db)


@router.post("/", status_code = 201)
def create(request: schemas.MCQS, db : Session = Depends(get_db)):
    return mcq.create_mcq(request, db)
    


@router.delete("/{id}")
def deletor(id,db : Session = Depends(get_db)):
    return mcq.delete_mcq(id,db)
    
    


@router.put("/{id}",status_code = 202)
def updator(request: schemas.MCQS, id, db : Session = Depends(get_db)):
    return mcq.update_mcq(request,id,db)


@router.get("/{id}",response_model=schemas.show_mcqs)
def reader(id: int,response: Response, db: Session = Depends(get_db)):
    return mcq.get_mcq(id,db)


