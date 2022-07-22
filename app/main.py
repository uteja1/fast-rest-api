from random import randrange
from fastapi import FastAPI, HTTPException, Response, status
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


def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i


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


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/post/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return post_dict
