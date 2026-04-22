from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://samrat:ghost@localhost/primetrade"

engine =create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=0
    )


SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()