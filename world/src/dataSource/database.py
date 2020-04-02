import mysql.connector

from core.logging_handler import Logging
from core.server_config import Config


class Database():
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''
    def __init__(self):
        self.log = Logging()
        self.log.debug('Database instance has been created')

    def initialize_data(self):
        pass

    #initialize_connection
    def get_connection(self):
        config = Config()
        config.initialize()
        try:
            connection = mysql.connector.connect(host=config.get_world_db_host(),
                                        port=config.get_world_db_port(),
                                        user=config.get_world_db_user(),
                                        password=config.get_world_db_passwo(),
                                        db=config.get_world_db_name(),
                                        auth_plugin='mysql_native_password')
            return connection

        except mysql.connector.Error as Error:
            self.log.warning('Database - initialize_connection\n' +
                            'Config: '+ str(config.get_world_db_host()) + ' - ' +
                            str(config.get_world_db_port()) + ' - ' +
                            str(config.get_world_db_user()) + ' - ' +
                            str(config.get_world_db_passwo()) + ' - ' +
                            str(config.get_world_db_name()) +
                            '\nDatabase - Something went wrong: {}'.format(str(Error)))
            return False
