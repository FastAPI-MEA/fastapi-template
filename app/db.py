import logging

import sqlalchemy
from databases import Database
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from .settings import settings


db = Database(settings.DB_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(settings.DB_URL, pool_size=3, max_overflow=0)
if not database_exists(engine.url):
    create_database(engine.url)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata.create_all(engine)


def get_db():
    """
    A dependency for working with PostgreSQL
    """
    try:
        db = LocalSession()
        yield db
    except Exception as e:
        logging.error(e)
    finally:
        db.close()
