from sqlalchemy.orm import Session
from fastapi import HTTPException
from MCQS import models, schemas

def get_all(db: Session):
    mcqs = db.query(models.mcqs).all()
    return mcqs

def create_mcq(request: schemas.MCQS, db: Session):
    new_mcq = models.mcqs(question = request.question, answer= request.answer, user_id = 1)
    db.add(new_mcq)
    db.commit()
    db.refresh(new_mcq)
    return new_mcq

def delete_mcq(mcq_id: int, db: Session):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == mcq_id).first()
    if not mcq:
        raise HTTPException(status_code = 404, detail = f'mcq with id {mcq_id} not found.')
    else:
        
        db.delete(mcq)
        db.commit()
        return 'destroyed'
    

def update_mcq(request: schemas.MCQS, mcq_id: int, db: Session):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == mcq_id)
    if not mcq:
        raise HTTPException(status_code=404, detail=f'mcq with id {mcq_id} not found')
    else:
        mcq.update({'question': request.question,'answer':request.answer},  synchronize_session=False)
        db.commit()
        return {"updated successfullyy"}
    

def get_mcq(mcq_id: int, db: Session):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == mcq_id).first()
    
    if not mcq:
        raise HTTPException(status_code = 404, detail=f'mcq with {mcq_id} not found')
 
    return mcq