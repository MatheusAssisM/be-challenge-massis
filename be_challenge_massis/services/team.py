from typing import List
from ..configs.postgres import Database
from ..repositories.team import TeamRepository


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
