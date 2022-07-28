from typing import Optional
from pydantic import BaseModel, StrictStr


class Post(BaseModel):
    title: StrictStr
    content: StrictStr
    published: bool = True
    # rating: Optional[int] = None
