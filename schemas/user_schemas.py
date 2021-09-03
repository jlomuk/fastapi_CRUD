from typing import Optional, List
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    is_active: bool


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass
