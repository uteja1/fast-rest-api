from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreateResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
