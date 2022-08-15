from sqlalchemy.orm import Session
from ..models.coach import Coach


class CoachRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def bulk_create(self, coach_list: list):
        coaches = [Coach(**coach) for coach in coach_list]
        with self.session_db() as session:
            session.bulk_save_objects(coaches, return_defaults=True)
            session.commit()
        return coaches
