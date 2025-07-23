from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.crud import crud
from app.models import models
from app.schemas import schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)

@router.put("/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}