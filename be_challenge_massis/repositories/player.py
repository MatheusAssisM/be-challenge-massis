from sqlalchemy.orm import Session
from ..models.player import Player


class PlayerRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db
        self.player = Player

    def bulk_create(self, team_data_list: list):
        players = [self.player(**team) for team in team_data_list]
        with self.session_db() as session:
            session.bulk_save_objects(players)
            session.commit()
        return players
