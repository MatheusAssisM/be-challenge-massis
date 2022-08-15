from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, text
from sqlalchemy.orm import relationship
from .team_league_association import teams_leagues_association

from .base import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    tla = Column(String(length=3))
    short_name = Column(String(length=30))
    area_name = Column(String(length=50), nullable=False)
    address = Column(String(length=255), nullable=False)
    football_id = Column(Integer)
    last_api_update = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    leagues = relationship(
        "League",
        secondary=teams_leagues_association,
        back_populates="teams",
        lazy="joined",
    )
    players = relationship("Player", back_populates="team", lazy="joined")
    coaches = relationship("Coach", back_populates="team")
