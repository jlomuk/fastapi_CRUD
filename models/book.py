import sqlalchemy as sa
from sqlalchemy.orm import relationship

from core.database import Base


class Book(Base):
    __tablename__ = 'books'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    author = sa.Column(sa.String, nullable=False)
    price = sa.Column(sa.Numeric(8, 2))
    date_publish = sa.Column(sa.DateTime)
    owner_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('users.id', ondelete='cascade'), nullable=True
    )
    owner = relationship('models.user.User', back_populates='books')
