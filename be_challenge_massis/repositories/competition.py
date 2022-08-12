from sqlalchemy.orm import Session
from ..models.competition import Competition


class Competition:
    def __init__(self, session_db: Session):
        self.session_db = session_db
        self.competition = Competition
