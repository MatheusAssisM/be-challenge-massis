from sqlalchemy.orm import Session
from ..models.team import Team


class TeamRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db
        self.team = Team

    def bulk_create(self, team_data_list: list):
        teams = [self.team(**team) for team in team_data_list]
        with self.session_db() as session:
            session.bulk_save_objects(teams)
            session.commit()
        return teams

