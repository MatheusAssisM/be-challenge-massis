from fastapi import HTTPException

from ..configs.postgres import Database
from ..repositories.league import LeagueRepository


class LeagueService:
    def __init__(
        self,
        postgres: Database,
    ):
        self.league_repository = LeagueRepository(postgres.session)

    def get_league(self, league_code: str):
        if not league_code:
            raise HTTPException(400, detail="Invalid league code")
        return self.league_repository.get_by_code(league_code)
