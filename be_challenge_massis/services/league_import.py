import json
from typing import List

from fastapi import HTTPException

from ..configs.postgres import Database
from ..helpers.league_import import format_date_of_birth, format_datetime
from ..models import League, Team
from ..repositories import (
    CoachRepository,
    LeagueRepository,
    PlayerRepository,
    TeamRepository,
)
from ..services import FootballAPIService, LeagueService, TeamService


class LeagueImportService:
    def __init__(
        self,
        postgres: Database,
        football_api_service: FootballAPIService,
        league_service: LeagueService,
        team_service: TeamService,
    ):
        self.league_repository = LeagueRepository(postgres.session)
        self.team_repository = TeamRepository(postgres.session)
        self.player_repository = PlayerRepository(postgres.session)
        self.coach_repository = CoachRepository(postgres.session)
        self.football_api_service = football_api_service
        self.league_service = league_service
        self.team_service = team_service

    def import_league_data(self, league_code: str):
        league_db = self.league_service.get_league(league_code)
        league = self.football_api_service.get_league(league_code)
        self.check_league_update(league_db, league)

        league_data = self.prepare_league_data(league)
        league_db = self.league_repository.create(league_data)

        league_teams = self.football_api_service.get_league_teams(league_code)
        teams_db = self.team_service.get_existing_teams(league_teams)
        teams = self.prepare_teams_data(league_teams, teams_db)
        new_teams = self.team_repository.bulk_create(teams)
        teams_to_associate = new_teams + teams_db

        if new_teams:
            players, coaches = self.prepare_team_composition(league_teams, new_teams)
            self.coach_repository.bulk_create(coaches)
            self.player_repository.bulk_create(players)

        self.league_repository.associate_team_league(league_db, teams_to_associate)
        return "League data imported successfully!"

    def prepare_league_data(self, league: dict):
        return {
            "name": league["name"],
            "code": league["code"],
            "area_name": league["area"]["name"],
            "football_id": league["id"],
            "last_api_update": format_datetime(league["lastUpdated"]),
        }

    def check_league_update(self, league_db: League, league: dict):
        if not league_db:
            return False
        last_update_db = league_db.last_api_update
        last_update_api = format_datetime(league["lastUpdated"])
        if last_update_db <= last_update_api:
            raise HTTPException(
                status_code=409,
                detail="League data is already up to date!",
            )
        return True

    def prepare_teams_data(self, teams: List[dict], teams_db: List[Team]):
        teams_data = []
        teams_db_id = [team.football_id for team in teams_db]
        for team in teams:
            if team["id"] in teams_db_id:
                continue
            teams_data.append(
                {
                    "name": team["name"],
                    "tla": team["tla"],
                    "short_name": team["shortName"],
                    "address": team["address"],
                    "football_id": team["id"],
                    "area_name": team["area"]["name"],
                    "last_api_update": format_datetime(team["lastUpdated"]),
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
            "football_id": coach_data["id"],
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
