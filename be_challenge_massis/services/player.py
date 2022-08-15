from fastapi import HTTPException

from ..configs.postgres import Database
from ..repositories.player import PlayerRepository
from ..services import LeagueService


class PlayerService:
    def __init__(
        self,
        postgres: Database,
        league_service: LeagueService,
    ):
        self.player_repository = PlayerRepository(postgres.session)
        self.league_service = league_service

    def get_players_by_league_and_team(self, league_code: str, team_name: str):
        league_db = self.league_service.get_league(league_code)
        if not league_db:
            raise HTTPException(404, detail="League not found")

        league_teams = league_db.teams
        if team_name:
            league_teams = [team for team in league_teams if team_name in team.name]

        league_players = []
        for team in league_teams:
            league_players.extend(team.players)
        return league_players
