from random import randrange
from urllib import response
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import StrictInt
from models.post import Post

app = FastAPI()

my_posts = [
    {
        "id": 1,
        "title": "beaches in florida",
        "content": "check out these beaches",
    },
    {
        "id": 2,
        "title": "pizza in florida",
        "content": "check out these pizza",
    },
]


@app.get("/")
async def getHello():
    return {"messege": "Hello World"}


@app.get("/posts")
def get_posts():
    return my_posts


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


@app.get("/post/{id}")
def get_post(id: int, response: Response):

    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"{id} Not Found"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    return post


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    new_post_dict = new_post.dict()
    new_post_dict["id"] = randrange(0, 5000)
    my_posts.append(new_post_dict)
    return new_post_dict
