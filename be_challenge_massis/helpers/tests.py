from ..configs.postgres import Postgres

postgres = Postgres("sqlite:///./test.db")
ENGINE = postgres.engine


def override_postgres_session():
    return postgres
