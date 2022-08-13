from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, text

from .base import Base


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    code = Column(String(length=10), nullable=False, unique=True)
    area_name = Column(String(length=50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    UniqueConstraint("code", name="unique_code")
