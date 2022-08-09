from app.db.handlers.posts_handler import (
    delete_post_by_id_handler,
    get_post_by_id_handler,
    persist_new_post_handler,
    update_post_by_id_handler,
)
from app.models.post import Post
from sqlalchemy.orm import Session


def create_post_executor(db: Session, new_post: Post):
    new_post_created = persist_new_post_handler(db=db, new_post=new_post)
    return new_post_created


def get_post_by_id_executor(db: Session, id: int):
    post = get_post_by_id_handler(db, id)
    return post


def delete_post_by_id_executor(db: Session, id: int):
    deleted_post = delete_post_by_id_handler(db, id)
    return deleted_post


def update_post_by_id_executor(db: Session, id: int, post: Post):
    updated_post = update_post_by_id_handler(db, id, post)
    return updated_post
