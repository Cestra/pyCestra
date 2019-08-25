import sys

import pymysql.connections

from core.config import Config
from core.logging_handler import Log


class Database():
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''
    def __init__(self):
        self.log = Log()
        self.log.debug('Database instance has been created')

    def initialize_data(self):
        pass
        
    #initialize_connection
    def get_connection(self):
        config = Config()
        config.initialize()
        try:
            self.__connection = pymysql.connect(host=config.get_host(),
                                              port=config.get_port(),
                                              user=config.get_user(),
                                              password=config.get_pass(),
                                              db=config.get_database_name())
            return self.__connection

        except pymysql.Error as Error:
            self.log.warning('Database - initialize_connection\n' +
                  'Config: '+config.get_host()+config.get_port()+config.get_user()+config.get_pass()+config.get_database_name() +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            return False