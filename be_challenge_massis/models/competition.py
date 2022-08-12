from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, text


class Competition(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    code = Column(String(length=10), nullable=False)
    area_name = Column(String(length=50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))
