import os

import requests
from fastapi import HTTPException
from redis import Redis
from datetime import timedelta

from ..helpers.football_api import RATE_LIMIT_KEY, REQUEST_LIMIT

FOOTBALL_API_URL = os.getenv("FOOTBALL_API_URL")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")


class FootballAPIService:
    def __init__(self, redis_client: Redis):
        self._headers = self._set_token_header()
        self.redis_client = redis_client

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

        self.check_rate_limit()
        if result.status_code != 200:
            raise HTTPException(
                status_code=result.status_code, detail="Impossible to get this league"
            )
        return result.json()

    def check_rate_limit(self):
        if self.redis_client.setnx(RATE_LIMIT_KEY, REQUEST_LIMIT):
            one_minute = timedelta(minutes=1).total_seconds()
            self.redis_client.expire(RATE_LIMIT_KEY, int(one_minute))
        actual_count = self.redis_client.get(RATE_LIMIT_KEY)
        if actual_count and int(actual_count) > 0:
            self.redis_client.decrby(RATE_LIMIT_KEY, 1)
            return False
        raise HTTPException(
            status_code=429, detail="Too many requests, please try again later"
        )

    def _set_token_header(self):
        return {"X-Auth-Token": FOOTBALL_API_KEY}
