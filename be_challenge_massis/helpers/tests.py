import json
from ..configs.postgres import Database
import fakeredis

with open("./be_challenge_massis/helpers/mock_data/league_response.json") as f:
    league_output = json.load(f)

with open("./be_challenge_massis/helpers/mock_data/league_teams_response.json") as f:
    teams_output = json.load(f)

sqlite = Database("sqlite:///test.db")
ENGINE = sqlite.engine

redis_server = fakeredis.FakeServer()


def override_sqlite3_session():
    return sqlite


def override_redis_db():
    redis_client = fakeredis.FakeStrictRedis(server=redis_server)
    yield redis_client
    redis_client.close()
