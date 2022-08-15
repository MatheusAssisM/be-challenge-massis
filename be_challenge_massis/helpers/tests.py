from ..configs.postgres import Database
import fakeredis

sqlite = Database("sqlite:///test.db")

ENGINE = sqlite.engine

redis_server = fakeredis.FakeServer()


def override_sqlite3_session():
    return sqlite


def override_redis_db():
    redis_client = fakeredis.FakeStrictRedis(server=redis_server)
    yield redis_client
    redis_client.close()
