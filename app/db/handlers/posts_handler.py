from http.client import HTTPException
from fastapi import status
from app.db.models.posts_vo import Post_VO
from app.schemas.post import Post
from sqlalchemy.orm import Session
from ..db_base import Base, get_db, db_session


def persist_new_post_handler(db: Session, new_post: Post):

    new_post_created = Post_VO(
        title=new_post.title, content=new_post.content, published=new_post.published
    )
    db.add(new_post_created)
    db.commit()
    db.refresh(new_post_created)

    return new_post_created


def get_post_by_id_handler(db: Session, id: int):
    post = db.query(Post_VO).filter(Post_VO.id == id).first()
    return post


def delete_post_by_id_handler(db: Session, id: int):
    deleted_post = db.query(Post_VO).get(id)
    if deleted_post == None:
        return None
    db.delete(deleted_post)
    db.commit()
    return deleted_post


def update_post_by_id_handler(db: Session, id: int, post_update: Post):
    post_query = db.query(Post_VO).filter(Post_VO.id == id)
    post = post_query.first()
    if post == None:
        return None
    post_query.update(post_update.dict(), synchronize_session=False)
    db.commit()
    updated_post = post_query.first()
    return updated_post
