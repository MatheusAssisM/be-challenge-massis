from be_challenge_massis.dependencies.databases import (
    get_postgres_session,
    get_redis_client,
)
from be_challenge_massis.main import app
from be_challenge_massis.models.base import Base
from fastapi.testclient import TestClient

from pytest import fixture

from ..helpers.tests import ENGINE, override_sqlite3_session, override_redis_db

app.dependency_overrides[get_postgres_session] = override_sqlite3_session
app.dependency_overrides[get_redis_client] = override_redis_db


@fixture
def client():
    Base.metadata.create_all(bind=ENGINE)
    _client = TestClient(app)
    yield _client
    Base.metadata.drop_all(bind=ENGINE)


@fixture
def sqlite():
    return override_sqlite3_session
