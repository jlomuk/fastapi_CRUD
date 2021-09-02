from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.db_url.format(
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.db_name
), pool_pre_ping=True, echo=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def initdb():
    import models.book
    import models.user
    Base.metadata.create_all(engine)
