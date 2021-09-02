import sqlalchemy as sa
from sqlalchemy.orm import relationship

from core.database import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, index=True)
    password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
    books = relationship('Book', back_populates="owner")
