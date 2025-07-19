from sqlalchemy import Column, Integer, String, DateTime, func
from app.db import Base

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(String(2000), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())