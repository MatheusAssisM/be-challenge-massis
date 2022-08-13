from sqlalchemy.orm import Session
from ..models.league import League


class LeagueRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db
        self.league = League

    def create(self, league_data: dict):
        league = self.league(**league_data)
        with self.session_db() as session:
            session.add(league)
            session.commit()
        return league

    def get_by_code(self, league_code: str):
        with self.session_db() as session:
            return session.query(self.league).filter_by(code=league_code).first()
