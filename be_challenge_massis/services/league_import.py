import json

from fastapi import HTTPException

from ..configs.postgres import Postgres
from ..repositories.league import LeagueRepository
from ..services.football_api import FootballAPIService


class LeagueImportService:
    def __init__(
        self,
        postgres: Postgres,
        football_api_service: FootballAPIService,
    ):
        self.league_repository = LeagueRepository(postgres.session)
        self.football_api_service = football_api_service

    def import_league(self, league_code: str):
        # with open("./be_challenge_massis/helpers/mock_football_data.json", "r") as f:
        #     response = json.load(f)

        response = self.football_api_service.get_league(league_code)
        if self.check_league_exists(league_code):
            raise HTTPException(
                status_code=409, detail="This League was already imported"
            )

        league_data = self.prepare_league_data(response)
        self.league_repository.create(league_data)
        return "League imported successfully"

    def prepare_league_data(self, league: dict):
        return {
            "name": league["name"],
            "code": league["code"],
            "area_name": league["area"]["name"],
        }

    def check_league_exists(self, league_code: str):
        return self.league_repository.get_by_code(league_code)
