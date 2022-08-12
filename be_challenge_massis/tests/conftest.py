from fastapi.testclient import TestClient
from pytest import fixture

from be_challenge_massis.dependencies.databases import get_postgres_session
from be_challenge_massis.helpers.tests import ENGINE, override_postgres_session
from be_challenge_massis.main import app
from be_challenge_massis.models.base import Base


app.dependency_overrides[get_postgres_session] = override_postgres_session


@fixture
def client():
    Base.metadata.create_all(bind=ENGINE)
    _client = TestClient(app)
    yield _client
    Base.metadata.drop_all(bind=ENGINE)


@fixture
def session_db():
    return override_postgres_session
