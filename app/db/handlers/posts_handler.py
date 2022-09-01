from sqlalchemy.orm import Session


from app.db.models.posts_vo import Post_VO
from app.schemas.post import Post


def persist_new_post_handler(db: Session, new_post: Post):

    new_post = Post_VO(
        title=new_post.title, content=new_post.content, published=new_post.published
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


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
