from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

from app.db.db_base import get_db
from app.schemas.user_create import UserCreate
from app.executors.user_executor import create_user_executor, get_user_executor
from app.schemas.user_create_response import UserCreateResponse

router = APIRouter()


@router.post(
    "/user",
    status_code=status.HTTP_201_CREATED,
    response_model=UserCreateResponse,
)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    new_user_created = create_user_executor(db, new_user)
    return new_user_created


@router.get(
    "/user/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UserCreateResponse,
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = get_user_executor(db, id)
    return user
