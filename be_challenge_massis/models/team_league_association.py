from sqlalchemy import ForeignKey, Column, Table

from .base import Base

teams_leagues_association = Table(
    "leagues_teams_association",
    Base.metadata,
    Column("league_id", ForeignKey("leagues.id"), primary_key=True),
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
)
