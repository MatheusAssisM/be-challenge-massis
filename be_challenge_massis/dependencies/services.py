from be_challenge_massis.services.league import LeagueService
from be_challenge_massis.services.football_api import FootballAPIService
from fastapi import Depends
from sqlalchemy.orm import Session
from .databases import get_postgres_session


def get_league_service(session_db: Session = Depends(get_postgres_session)):
    football_api_service = FootballAPIService()
    return LeagueService(session_db, football_api_service)
