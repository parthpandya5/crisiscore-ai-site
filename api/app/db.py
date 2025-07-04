import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ─── Database URL ─────────────────────────────────────────────────────────────
# You can also set this via the DATABASE_URL env var
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://parthpandya:P%40rthheysha2kk5@localhost:5432/crisiscore"
)

# ─── Engine & Session ──────────────────────────────────────────────────────────
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ─── Base for Models ───────────────────────────────────────────────────────────
Base = declarative_base()
