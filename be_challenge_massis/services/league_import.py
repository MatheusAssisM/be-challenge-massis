import json

from fastapi import HTTPException

from ..configs.postgres import Postgres
from ..repositories.league import LeagueRepository
from ..repositories.team import TeamRepository
from ..services.football_api import FootballAPIService


class LeagueImportService:
    def __init__(
        self,
        postgres: Postgres,
        football_api_service: FootballAPIService,
    ):
        self.league_repository = LeagueRepository(postgres.session)
        self.team_repository = TeamRepository(postgres.session)
        self.football_api_service = football_api_service

    def import_league(self, league_code: str):
        league = self.football_api_service.get_league(league_code)
        if self.check_league_exists(league_code):
            raise HTTPException(
                status_code=409, detail="This League was already imported"
            )

        league_data = self.prepare_league_data(league)
        self.league_repository.create(league_data)

        team_ids = self.get_teams_ids(league["seasons"])
        teams = self.football_api_service.get_teams(team_ids)
        teams_data = self.prepare_teams_data(teams)
        self.team_repository.bulk_create(teams_data)

        return "League imported successfully"

    def prepare_league_data(self, league: dict):
        return {
            "name": league["name"],
            "code": league["code"],
            "area_name": league["area"]["name"],
        }

    def check_league_exists(self, league_code: str):
        return self.league_repository.get_by_code(league_code)

    def get_teams_ids(self, seasons: list):
        team_ids = {season["winner"]["id"] for season in seasons if season["winner"]}
        return team_ids

    def prepare_teams_data(self, teams):
        teams_data = []
        for team in teams:
            teams_data.append(
                {
                    "name": team["name"],
                    "tla": team["tla"],
                    "short_name": team["shortName"],
                    "address": team["address"],
                    "area_name": team["area"]["name"],
                }
            )
        return teams_data
