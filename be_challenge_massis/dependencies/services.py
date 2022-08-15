from fastapi import Depends
from sqlalchemy.orm import Session

from ..services.player import PlayerService

from ..services import (
    FootballAPIService,
    LeagueImportService,
    LeagueService,
    TeamService,
)
from .databases import get_postgres_session


def get_league_import_service(session_db: Session = Depends(get_postgres_session)):
    football_api_service = FootballAPIService()
    league_service = LeagueService(session_db)
    team_service = TeamService(session_db)
    return LeagueImportService(
        session_db, football_api_service, league_service, team_service
    )


def get_league_service(session_db: Session = Depends(get_postgres_session)):
    return LeagueService(session_db)


def get_player_service(session_db: Session = Depends(get_postgres_session)):
    league_service = LeagueService(session_db)
    return PlayerService(session_db, league_service)
