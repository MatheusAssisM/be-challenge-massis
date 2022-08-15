from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from redis import Redis
import json

from ..configs.postgres import Database
from ..repositories.player import PlayerRepository
from ..services import LeagueService
from ..helpers.player import LEAGUE_PLAYERS_KEY, ONE_MINUTE


class PlayerService:
    def __init__(
        self,
        postgres: Database,
        redis_client: Redis,
        league_service: LeagueService,
    ):
        self.player_repository = PlayerRepository(postgres.session)
        self.league_service = league_service
        self.redis_client = redis_client

    def get_players_by_league_and_team(self, league_code: str, team_name: str):
        key_cache = LEAGUE_PLAYERS_KEY.format(league_code, team_name)
        cached_data = self.redis_client.get(key_cache)
        if cached_data:
            return json.loads(cached_data)

        league_db = self.league_service.get_league(league_code)
        if not league_db:
            raise HTTPException(404, detail="League not found")

        league_teams = league_db.teams
        if team_name:
            league_teams = [team for team in league_teams if team_name in team.name]

        league_players = []
        for team in league_teams:
            league_players.extend(team.players)

        self.redis_client.setex(
            key_cache,
            ONE_MINUTE,
            json.dumps(jsonable_encoder(league_players)),
        )
        return league_players
