from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas
from ..utlis.hashing import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def update_user(db: Session, user_id: int, user_data: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    user.name = user_data.name
    user.email = user_data.email
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    return db.query(models.Post).all()


def get_user_posts(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    return user.posts  
