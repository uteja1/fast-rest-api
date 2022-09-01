from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from app.db.db_base import get_db
from app.executors.posts_executor import (
    create_post_executor,
    delete_post_by_id_executor,
    get_post_by_id_executor,
    update_post_by_id_executor,
)
from app.schemas.post import Post
from app.schemas.post_response import PostResponse

router = APIRouter()


@router.get("/")
async def getHello():
    return {"messege": "Hello World"}


@router.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = get_post_by_id_executor(db, id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return post


@router.post("/post", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(new_post: Post, db: Session = Depends(get_db)):
    new_post_created = create_post_executor(db, new_post)
    return new_post_created


@router.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    deleted_post = delete_post_by_id_executor(db, id)
    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return deleted_post


@router.put("/post/{id}", response_model=PostResponse)
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    updated_post = update_post_by_id_executor(db, id, post)
    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return updated_post
