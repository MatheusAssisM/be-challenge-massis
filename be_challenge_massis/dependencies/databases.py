import os

from ..configs.postgres import Database
from ..configs.redis import RedisClient

DB_NAME = os.getenv("DB_NAME", "football")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "be-challenge-massis-postgres.com")
DB_PORT = os.getenv("DB_PORT", "5432")
REDIS_HOST = os.getenv("REDIS_HOST", "be-challenge-massis-redis.com")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

POSTGRES_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_postgres_session():
    return Database(POSTGRES_DATABASE_URL)


def get_redis_client():
    return RedisClient(host=REDIS_HOST, port=int(REDIS_PORT)).get_conn()
