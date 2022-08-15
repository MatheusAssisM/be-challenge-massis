from ..configs.postgres import Database

sqlite = Database("sqlite:///test.db")

ENGINE = sqlite.engine


def override_sqlite3_session():
    return sqlite
