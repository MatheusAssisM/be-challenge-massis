from fastapi import Depends
from redis import Redis
from sqlalchemy.orm import Session

from ..services import (
    FootballAPIService,
    LeagueImportService,
    LeagueService,
    TeamService,
)
from ..services.player import PlayerService
from .databases import get_postgres_session, get_redis_client


def get_league_import_service(
    session_db: Session = Depends(get_postgres_session),
    redis_client: Redis = Depends(get_redis_client),
):
    football_api_service = FootballAPIService(redis_client)
    league_service = LeagueService(session_db)
    team_service = TeamService(session_db)
    return LeagueImportService(
        session_db, football_api_service, league_service, team_service
    )


def get_player_service(
    session_db: Session = Depends(get_postgres_session),
    redis_client: Redis = Depends(get_redis_client),
):
    league_service = LeagueService(session_db)
    return PlayerService(session_db, redis_client, league_service)


def get_team_service(
    session_db: Session = Depends(get_postgres_session),
    redis_client: Redis = Depends(get_redis_client),
):
    return TeamService(session_db, redis_client)
