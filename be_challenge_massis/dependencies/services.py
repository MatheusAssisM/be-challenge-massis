from fastapi import Depends
from sqlalchemy.orm import Session

from ..services.football_api import FootballAPIService
from ..services.league_import import LeagueImportService
from .databases import get_postgres_session


def get_league_service(session_db: Session = Depends(get_postgres_session)):
    football_api_service = FootballAPIService()
    return LeagueImportService(session_db, football_api_service)
