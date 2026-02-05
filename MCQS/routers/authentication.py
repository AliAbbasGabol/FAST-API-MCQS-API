from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, hashing
from . import jwt_gen
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.users).filter(models.users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no user with email {request.username}")
    else:
        if hashing.Hash.verify(request.password,user.password):
            access_token = jwt_gen.create_access_token(data={"sub": user.email})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="Wrong password or email")
