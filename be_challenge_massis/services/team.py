import json
from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from redis import Redis

from ..configs.postgres import Database
from ..helpers.team import ONE_MINUTE, TEAM_BY_ID_KEY, TEAM_BY_NAME_KEY
from ..repositories.team import TeamRepository


class TeamService:
    def __init__(
        self,
        postgres: Database,
        redis_client: Redis,
    ):
        self.team_repository = TeamRepository(postgres.session)
        self.redis_client = redis_client

    def get_existing_teams(self, teams: List[dict]):
        teams_id = [int(team["id"]) for team in teams]
        teams_db = self.team_repository.get_existing_teams(teams_id)
        return teams_db or []

    def get_team_by_name(self, team_name: str, players: bool):
        key_cache = TEAM_BY_NAME_KEY.format(team_name, players)
        cached_data = self.redis_client.get(key_cache)
        if cached_data:
            return json.loads(cached_data)

        team_db = self.team_repository.get_team_by_name(team_name)
        if not team_db:
            raise HTTPException(status_code=404, detail="This team does not exist!")

        if not players:
            del team_db.players

        self.redis_client.setex(
            key_cache,
            ONE_MINUTE,
            json.dumps(jsonable_encoder(team_db)),
        )
        return team_db

    def get_by_id(self, team_id: int):
        key_cache = TEAM_BY_ID_KEY.format(team_id)
        cached_data = self.redis_client.get(key_cache)
        if cached_data:
            return json.loads(cached_data)

        team_db = self.team_repository.get_by_id(team_id)
        if not team_db:
            raise HTTPException(status_code=404, detail="This team does not exist!")

        if team_db.players:
            del team_db.coaches

        self.redis_client.setex(
            key_cache,
            ONE_MINUTE,
            json.dumps(jsonable_encoder(team_db)),
        )
        return team_db
