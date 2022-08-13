from pydantic import BaseModel


class ImportLeague(BaseModel):
    league_code: str
