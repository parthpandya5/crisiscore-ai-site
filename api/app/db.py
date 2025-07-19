import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Prefer environment variable; fall back to hard-coded local dev URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://parthpandya5:P%40rthheysha2kk5@localhost:5432/crisiscore"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
