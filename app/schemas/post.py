from typing import Optional
from pydantic import BaseModel, StrictStr

from app.schemas.post_base import PostBase


class Post(PostBase):
    pass
    # rating: Optional[int] = None
