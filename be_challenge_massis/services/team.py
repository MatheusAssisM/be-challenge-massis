from typing import List
from ..configs.postgres import Database
from ..repositories.team import TeamRepository
from fastapi import HTTPException


class TeamService:
    def __init__(
        self,
        postgres: Database,
    ):
        self.team_repository = TeamRepository(postgres.session)

    def get_existing_teams(self, teams: List[dict]):
        teams_id = [int(team["id"]) for team in teams]
        teams_db = self.team_repository.get_existing_teams(teams_id)
        return teams_db or []

    def get_team_by_name(self, team_name: str, players: bool):
        team_db = self.team_repository.get_team_by_name(team_name)
        if not team_db:
            raise HTTPException(status_code=404, detail="This team does not exist!")

        if not players:
            del team_db.coaches
            del team_db.players

        return team_db
