from fastapi import Depends, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
def get_user(user_id: int, db: Session):
    user = db.query(models.users).filter(models.users.id == user_id).first()
    if not user:
        raise HTTPException(status_code= 404, detail= "user not found")
    else:
        return user
    

def create_user(request: schemas.user, db: Session):
    new_user = models.users(name = request.name, email = request.email,password = Hash.encryptor(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user