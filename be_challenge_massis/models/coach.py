from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from .base import Base


class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    nationality = Column(String(length=50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    football_id = Column(Integer)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="coaches")
