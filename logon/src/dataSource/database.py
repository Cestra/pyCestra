import sys

import pymysql.connections

from core.config import Config


class Database():
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''
    def __init__(self):
        print('[DEBUG] Database instance has been created')

    def initialize_data(self):
        pass
        
    #initialize_connection
    def getConnection(self):
        try:
            config = Config()
            config.initialize()
        except:
            print('[ERROR] Database - config.initialize()\n')
        try:
            self.__connection = pymysql.connect(host=config.get_host(),
                                              port=config.get_port(),
                                              user=config.get_user(),
                                              password=config.get_pass(),
                                              db=config.get_database_name())
            return self.__connection

        except pymysql.Error as Error:
            print('[ERROR] Database - initialize_connection\n' +
                  'Config: ', config.get_host(), config.get_port(), config.get_user(), config.get_pass(), config.get_database_name() +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            return False

    '''
    def test_connection(self):
        try:
            cursor = Database().initialize_connection()
            if cursor:
                cursor.execute('SELECT VERSION()')
                results = cursor.fetchone()
                if results:
                    cursor.close()
                    return True
                else:
                    return False
            else:
                return False
        except pymysql.Error as Error:
            print('Database - testConnection - Something went wrong: {}'.format(Error))
        return False
    '''