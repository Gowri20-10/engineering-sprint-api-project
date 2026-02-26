from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from app.core.database import Base

class AILog(Base):
    __tablename__ = "ai_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    prompt = Column(Text)
    response = Column(Text)
    tokens_used = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
