from typing import List
from sqlalchemy.orm import Session

from ..models.team import Team


class TeamRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def bulk_create(self, team_data_list: List[dict]):
        teams = [Team(**team) for team in team_data_list]
        with self.session_db() as session:
            session.bulk_save_objects(teams, return_defaults=True)
            session.commit()
        return teams or []

    def get_existing_teams(self, team_ids: List[int]):
        with self.session_db() as session:
            return session.query(Team).filter(Team.football_id.in_(team_ids)).all()
