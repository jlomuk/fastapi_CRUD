import sqlalchemy as sa
from sqlalchemy.orm import relationship

from core.database import Base
from models.book import Book


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True, nullable=False)
    books = relationship(Book, back_populates="owner")

    def __repr__(self) -> str:
        return f'{self.id}: {self.email}'
