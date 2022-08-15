import redis


class Singleton(type):
    """
    An metaclass for singleton purpose. Every singleton class should inherit from this class by 'metaclass=Singleton'.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisClient(metaclass=Singleton):
    def __init__(self, host: str, port: int):
        self.pool = redis.ConnectionPool(host=host, port=int(port))

    @property
    def conn(self):
        if not hasattr(self, "_conn"):
            self.get_connection()
        return self._conn

    def get_connection(self):
        self._conn = redis.Redis(connection_pool=self.pool)

    @staticmethod
    def get_conn():
        redis_client = RedisClient()
        return redis_client.conn
