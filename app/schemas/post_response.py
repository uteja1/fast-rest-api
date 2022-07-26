from datetime import datetime

from app.schemas.post_base import PostBase


class PostResponse(PostBase):
    id: int
    created_at: datetime
    # rating: Optional[int] = None

    class Config:
        orm_mode = True
