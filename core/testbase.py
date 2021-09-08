from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base

from settings import settings

engine = create_engine(settings.db_url.format(
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.test_db_name
), pool_pre_ping=True)

Session: sessionmaker = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_test_db() -> None:
    import models.book
    import models.user
    Base.metadata.create_all(engine)


def drob_test_db() -> None:
    import models.book
    import models.user
    Base.metadata.drop_all(engine)


def get_test_session() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()
