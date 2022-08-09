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
from .models.post import Post
import time

# from .db.database import get_db
from .db.models.posts_vo import Post_VO, Base
from sqlalchemy.orm import Session

app = FastAPI()

# Base.metadata.create_all(bind=engine)

# my_posts = [
#     {
#         "id": 1,
#         "title": "beaches in florida",
#         "content": "check out these beaches",
#     },
#     {
#         "id": 2,
#         "title": "pizza in florida",
#         "content": "check out these pizza",
#     },
# ]

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fast-api-db",
            user="postgres",
            password="admin",
            cursor_factory=RealDictCursor,
        )

        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("connecting to database failed : ", error)
        time.sleep(5)


# @app.get("/getPostgres")
# def test_posts(db: Session = Depends(get_db)):
#     get_posts = db.query(Post_VO).all()
#     return {"data": get_posts}


@app.get("/")
async def getHello():
    return {"messege": "Hello World"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post


# def find_index_post(id):
#     for i, post in enumerate(my_posts):
#         if post["id"] == id:
#             return i


@app.get("/post/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()
    post = get_post_by_id_executor(db, id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"{id} Not Found"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return {"data": post}


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post, db: Session = Depends(get_db)):
    # new_post_dict = new_post.dict()
    # new_post_dict["id"] = randrange(0, 5000)
    # my_posts.append(new_post_dict)
    # cursor.execute(
    #     """ INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #     (new_post.title, new_post.content, new_post.published),
    # )
    # conn.commit()
    # new_post_added = cursor.fetchone()

    new_post_created = create_post_executor(db, new_post)
    return {"data": new_post_created}


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # index = find_index_post(id)

    # cursor.execute(""" DELETE FROM posts WHERE id = %s  returning *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    deleted_post = delete_post_by_id_executor(db, id)
    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    # my_posts.pop(index)

    return deleted_post


@app.put("/post/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    # index = find_index_post(id)

    # cursor.execute(
    #     "UPDATE posts SET title = %s ,content = %s ,published = %s WHERE id = %s returning * ",
    #     (
    #         post.title,
    #         post.content,
    #         post.published,
    #         str(id),
    #     ),
    # )
    # updated_post = cursor.fetchone()
    # conn.commit()

    updated_post = update_post_by_id_executor(db, id, post)
    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    # post_dict = post.dict()
    # post_dict["id"] = id
    # my_posts[index] = post_dict
    return {"data": updated_post}
