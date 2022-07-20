from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, StrictStr

app = FastAPI()


@app.get("/")
async def getHello():
    return {"messege": "Hello World"}


@app.get("/getposts")
def get_posts():
    return {"data": "This is your posts"}


class Post(BaseModel):
    title: StrictStr
    content: StrictStr
    published: bool = True
    rating: Optional[int] = None


@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post.title)
    return new_post
