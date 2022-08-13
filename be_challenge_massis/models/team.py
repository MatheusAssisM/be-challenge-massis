from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, text

from .base import Base


class League(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    tla = Column(String(length=3), nullable=False, unique=True)
    short_name = Column(String(length=30), nullable=False)
    area_name = Column(String(length=50), nullable=False)
    address = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    UniqueConstraint("name", name="name_unique")
