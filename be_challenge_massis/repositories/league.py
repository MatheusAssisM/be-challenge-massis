from typing import List
from sqlalchemy.orm import Session

from ..models.team import Team
from ..models.league import League


class LeagueRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def create(self, league_data: dict):
        league = League(**league_data)
        with self.session_db() as session:
            session.add(league)
            session.commit()
            session.refresh(league)
        return league

    def associate_team_league(self, league: League, teams: List[Team]):
        for team in teams:
            league.teams.append(team)

        with self.session_db() as session:
            session.add(league)
            session.commit()

    def get_by_code(self, league_code: str):
        with self.session_db() as session:
            return session.query(League).filter_by(code=league_code).first()
