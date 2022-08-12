import os
from ...configs.postgres import Postgres

DB_NAME = os.getenv("DB_NAME", "football")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "be-challenge-massis-postgres.com")
DB_PORT = os.getenv("DB_PORT", "5432")

POSTGRES_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_postgres_session():
    return Postgres(POSTGRES_DATABASE_URL)
