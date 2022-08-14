from ..configs.postgres import Postgres
from ..repositories.league import LeagueRepository
from ..repositories.player import PlayerRepository
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
        self.player_repository = PlayerRepository(postgres.session)
        self.football_api_service = football_api_service

    def import_league(self, league_code: str):
        league = self.football_api_service.get_league(league_code)
        league_data = self.prepare_league_data(league)
        self.league_repository.create(league_data)

        league_teams = self.football_api_service.get_league_teams(league_code)
        teams_data = self.prepare_teams_data(league_teams)
        self.team_repository.bulk_create(teams_data)

        players_data = self.prepare_players_data(league_teams)
        self.player_repository.bulk_create(players_data)

        return "League imported successfully"

    def prepare_league_data(self, league: dict):
        return {
            "name": league["name"],
            "code": league["code"],
            "area_name": league["area"]["name"],
        }

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

    def prepare_players_data(self, teams: list):
        players_data = []
        for team in teams:
            for player in team["squad"]:
                players_data.append(
                    {
                        "name": player["name"],
                        "position": player["position"],
                        "date_of_birth": player["dateOfBirth"],
                        "nationality": player["nationality"],
                    }
                )
        return players_data
