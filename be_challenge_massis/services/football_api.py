import requests
from fastapi import HTTPException
import os

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
                status_code=result.status_code, detail="Impossible to get league"
            )
        return result.json()

    def _set_token_header(self):
        return {"X-Auth-Token": FOOTBALL_API_KEY}
