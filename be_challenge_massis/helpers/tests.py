from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


ENGINE = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
SESSION = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)


@contextmanager
def override_postgres_session():
    try:
        session = SESSION()
        yield session
    finally:
        session.close()
