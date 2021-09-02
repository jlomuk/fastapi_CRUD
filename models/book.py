import sqlalchemy as sa
from sqlalchemy.orm import relationship

from core.database import Base


class Book(Base):
    __tablename__ = 'books'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True, index=True)
    author = sa.Column(sa.String)
    price = sa.Column(sa.Numeric(8, 2))
    date_publish = sa.Column(sa.DateTime)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), default=None)
    owner = relationship('User', back_populates='books')
