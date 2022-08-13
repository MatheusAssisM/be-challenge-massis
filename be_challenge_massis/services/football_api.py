import os

import requests
from fastapi import HTTPException

FOOTBALL_API_URL = os.getenv("FOOTBALL_API_URL")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")


class FootballAPIService:
    def __init__(self):
        self._headers = self._set_token_header()

    def get_league(self, league_code: str):
        result = requests.get(
            f"{FOOTBALL_API_URL}/competitions/{league_code}", headers=self._headers
        )
        if result.status_code != 200:
            raise HTTPException(
                status_code=result.status_code, detail="Impossible to get this league"
            )
        return result.json()

    def get_teams(self, team_ids: list):
        teams = []
        for team_id in team_ids:
            result = requests.get(
                f"{FOOTBALL_API_URL}/teams/{team_id}", headers=self._headers
            )
            if result.status_code != 200:
                continue
            teams.append(result.json())
        return teams

    def _set_token_header(self):
        return {"X-Auth-Token": FOOTBALL_API_KEY}
