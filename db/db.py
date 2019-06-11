import configparser


class DatabaseConnector:
    """
    Database connector. Handles all basic database connections
    """
    __instance = None
    @staticmethod
    def get_instance():
        if __instance is None:
            DatabaseConnector()
        return DatabaseConnector.__instance

    def __init__(self,  host, user, passwd, port=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port if port is not None else 3306

        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='pynative_pool', pool_size=5,
                                                           pool_reset_session=True, host=self.host, database='fireflow',
                                                           user=self.user, password=self.passwd)
        except Error:
            print("[REALLY SHOULD LOG THIS!] Error getting connection pool")
            raise

    def signup(self, name, username, hash):
        connection = self.connection_pool.get_connection()

        if not connection.is_connected():
            # TODO: Add custom exception
            raise Error('not connected')
        
        