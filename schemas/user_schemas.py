from typing import Optional, List
from pydantic import BaseModel

from schemas.book_schemas import Book


class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    is_active: Optional[bool]


class User(UserBase):
    id: int
    books: List[Book]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
