from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictStr


class PostResponse(BaseModel):
    id: int
    title: StrictStr
    content: StrictStr
    published: bool = True
    created_at: datetime
    # rating: Optional[int] = None

    class Config:
        orm_mode = True
