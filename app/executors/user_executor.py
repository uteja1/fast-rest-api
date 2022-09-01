from sqlalchemy.orm import Session

from app.db.handlers.user_handler import (
    get_user_handler,
    persist_new_user_handler,
)
from app.schemas.user_create import UserCreate
from app.utils.utils import hash_password

def create_user_executor(db: Session, new_user: UserCreate):

    # hashed password
    new_user.password = hash_password(new_user.password)

    new_user_created = persist_new_user_handler(db=db, new_user=new_user)
    return new_user_created


def get_user_executor(db: Session, id: int):
    return get_user_handler(db, id)
