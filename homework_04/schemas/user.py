from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    username: str
    email: Optional[EmailStr]


class UserRead(UserBase):
    """
    Reads user
    """
    id: int

class UserCreate(UserBase):
    """
    Creates user
    """
