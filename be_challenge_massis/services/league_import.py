from typing import List
from fastapi import HTTPException

from ..configs.postgres import Database
from ..helpers.league_import import format_date_of_birth
from ..models.team import Team
from ..repositories.league import LeagueRepository
from ..repositories.player import PlayerRepository
from ..repositories.team import TeamRepository
from ..repositories.coach import CoachRepository
from ..services.football_api import FootballAPIService


class LeagueImportService:
    def __init__(
        self,
        postgres: Database,
        football_api_service: FootballAPIService,
    ):
        self.league_repository = LeagueRepository(postgres.session)
        self.team_repository = TeamRepository(postgres.session)
        self.player_repository = PlayerRepository(postgres.session)
        self.coach_repository = CoachRepository(postgres.session)
        self.football_api_service = football_api_service

    def import_league(self, league_code: str):
        if not league_code:
            raise HTTPException(400, detail="Invalid league code")
        league = self.football_api_service.get_league(league_code)
        league_data = self.prepare_league_data(league)
        league_db = self.league_repository.create(league_data)

        league_teams = self.football_api_service.get_league_teams(league_code)
        teams = self.prepare_teams_data(league_teams)
        teams_obj = self.team_repository.bulk_create(teams)

        self.league_repository.associate_team_league(league_db, teams_obj)

        players, coaches = self.prepare_team_composition(league_teams, teams_obj)
        self.coach_repository.bulk_create(coaches)
        self.player_repository.bulk_create(players)

        return "League imported successfully"

    def prepare_league_data(self, league: dict):
        return {
            "name": league["name"],
            "code": league["code"],
            "area_name": league["area"]["name"],
        }

    def prepare_teams_data(self, teams: List[dict]):
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

    def prepare_team_composition(self, teams: List[dict], teams_obj: List[Team]):
        players_data = []
        coaches_data = []
        teams = {team["name"]: team for team in teams}

        for team in teams_obj:
            team_data = teams[team.name]

            coach_data = team_data["coach"]
            print(coach_data)
            if coach_data.get("id"):
                coaches_data.append(self.prepare_coach_data(coach_data, team.id))

            team_squad = team_data.get("squad")
            if not team_squad:
                continue

            for player in team_squad:
                players_data.append(self.prepare_player_data(player, team.id))

        return players_data, coaches_data

    def prepare_coach_data(self, coach_data: dict, team_id: int):
        return {
            "name": coach_data["name"],
            "nationality": coach_data["nationality"],
            "date_of_birth": format_date_of_birth(coach_data["dateOfBirth"]),
            "team_id": team_id,
        }

    def prepare_player_data(self, player_data: dict, team_id: int):
        return {
            "name": player_data["name"],
            "position": player_data["position"],
            "date_of_birth": format_date_of_birth(player_data["dateOfBirth"]),
            "nationality": player_data["nationality"],
            "team_id": team_id,
        }
