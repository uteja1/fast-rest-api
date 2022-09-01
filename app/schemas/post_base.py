from pydantic import BaseModel, StrictStr


class PostBase(BaseModel):
    title: StrictStr
    content: StrictStr
    published: bool = True
    # rating: Optional[int] = None
