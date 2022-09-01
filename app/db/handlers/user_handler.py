from fastapi import status, HTTPException
from sqlalchemy.orm import Session


from app.db.models.user_vo import User_VO
from app.schemas.user_create import UserCreate


def persist_new_user_handler(db: Session, new_user: UserCreate):

    new_user = User_VO(**new_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_handler(db: Session, id: int):

    user = db.query(User_VO).filter(User_VO.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found"
        )

    return user
