from sqlalchemy import Column, Date, DateTime, Integer, String, text

from .base import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    position = Column(String(length=10), nullable=False)
    nationality = Column(String(length=50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))
