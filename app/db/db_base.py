from contextvars import ContextVar
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/fast-api-db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_session: ContextVar[Session] = ContextVar("db_session")

# @contextmanager
# def SessionManager():
#     db = SessionLocal()
#     try:
#         yield db
#     except:
#         # if we fail somehow rollback the connection
#         warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")
#         db.rollback()
#         raise
#     finally:
#         db.close()
