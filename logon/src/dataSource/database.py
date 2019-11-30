import sys

import pymysql.connections

from core.server_config import Config
from core.logging_handler import Logging


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
            connection = pymysql.connect(host=config.get_host(),
                                              port=config.get_port(),
                                              user=config.get_user(),
                                              password=config.get_pass(),
                                              db=config.get_database_name(),
                                              cursorclass=pymysql.cursors.DictCursor)
            return connection

        except pymysql.Error as Error:
            self.log.warning('Database - initialize_connection\n' +
                  'Config: '+ str(config.get_host()) + ' - ' +
                  str(config.get_port()) + ' - ' +
                  str(config.get_user()) + ' - ' +
                  str(config.get_pass()) + ' - ' +
                  str(config.get_database_name()) +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            return False
