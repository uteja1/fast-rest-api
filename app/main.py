from random import randrange
from turtle import title
from fastapi import Depends, FastAPI, HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from app.db.db_base import get_db

from app.executors.posts_executor import (
    create_post_executor,
    delete_post_by_id_executor,
    get_post_by_id_executor,
    update_post_by_id_executor,
)
from app.schemas.post_response import PostResponse
from .schemas.post import Post
import time

# from .db.database import get_db
from .db.models.posts_vo import Post_VO, Base
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
async def getHello():
    return {"messege": "Hello World"}


@app.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = get_post_by_id_executor(db, id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return post


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post, db: Session = Depends(get_db)):
    new_post_created = create_post_executor(db, new_post)
    return new_post_created


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    deleted_post = delete_post_by_id_executor(db, id)
    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return deleted_post


@app.put("/post/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    updated_post = update_post_by_id_executor(db, id, post)
    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return updated_post
