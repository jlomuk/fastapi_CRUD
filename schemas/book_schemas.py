from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str
    price: Decimal
    date_publish: datetime
    owner_id: int


class Book(BookBase):
    id: int


class BookCreate(BookBase):
    pass
