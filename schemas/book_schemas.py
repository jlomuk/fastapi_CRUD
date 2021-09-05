from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str
    price: Decimal
    date_publish: datetime
    owner_id: int


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass
