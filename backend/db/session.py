from email.generator import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from core.config import settings 

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

## lets create a local session
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

## lets add databse dependence 
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

        