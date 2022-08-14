import os

import requests
from fastapi import HTTPException

FOOTBALL_API_URL = os.getenv("FOOTBALL_API_URL")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")


class FootballAPIService:
    def __init__(self):
        self._headers = self._set_token_header()

    def get_league(self, league_code: str):
        url = f"{FOOTBALL_API_URL}/competitions/{league_code}"
        return self.make_request(url)

    def get_league_teams(self, league_code: str):
        url = f"{FOOTBALL_API_URL}/competitions/{league_code}/teams"
        response = self.make_request(url)
        return response["teams"]

    def make_request(self, url: str, method="get"):
        req_method = getattr(requests, method)
        result = req_method(url, headers=self._headers)
        if result.status_code != 200:
            raise HTTPException(
                status_code=result.status_code, detail="Impossible to get this league"
            )
        return result.json()

    def _set_token_header(self):
        return {"X-Auth-Token": FOOTBALL_API_KEY}
