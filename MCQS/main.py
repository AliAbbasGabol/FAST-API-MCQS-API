from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models, database
from .database import engine, session_local
from sqlalchemy.orm import Session


app = FastAPI()

models.base.metadata.create_all(engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/mcqs", status_code = 201)
def create(request: schemas.MCQS, db : Session = Depends(get_db)):
    new_mcq = models.mcqs(question = request.question, answer= request.answer)
    db.add(new_mcq)
    db.commit()
    db.refresh(new_mcq)
    return new_mcq

@app.delete("/mcqs/{id}")
def deletor(id,db : Session = Depends(get_db)):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == id).first()
    if not mcq:
        raise HTTPException(status_code = 404, detail = f'mcq with id {id} not found.')
    else:
        mcq.delete(synchronize_session = False)
        db.commit()
        return 'destroyed'


@app.put("/mcq/{id}",status_code = 202)
def updator(request: schemas.MCQS, id, db : Session = Depends(get_db)):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == id).first()
    if not mcq:
        raise HTTPException(status_code= 404, detail = f'mcq with id {id} not found')
    else:
        mcq.update({'question': request.question,'answer':request.answer},  synchronize_session=False)
        db.commit()
        return {"updated successfullyy"}




@app.get("/mcqs")
def read(db : Session = Depends(get_db)):
    mcqs = db.query(models.mcqs).all()
    return mcqs

@app.get("/mcqs/{id}")
def reader(id: int,response: Response, db: Session = Depends(get_db)):
    mcq = db.query(models.mcqs).filter(models.mcqs.id == id).first()
    
    if not mcq:
        raise HTTPException(status_code = 404, detail=f'mcq with {id} not found')
 
    return mcq