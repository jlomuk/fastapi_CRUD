from typing import Optional, List

from pydantic import BaseModel

from schemas.book_schemas import Book


class UserBase(BaseModel):
    email: str
    name: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    books: List[Book]


class UserCreate(UserBase):
    password: str
