import sys

import pymysql.connections

from core.config import Config


class Database:
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''
    def __init__(self):
        print('[DEBUG] Database instance has been created')

    def initialize_data(self):
        pass

    def initialize_connection(self):
        config = Config()
        config.initialize()
        try:
            self.connection = pymysql.connect(host=config.get_host(),
                                              port=config.get_port(),
                                              user=config.get_user(),
                                              password=config.get_pass(),
                                              db=config.get_database_name())

        except pymysql.Error as Error:
            print('[ERROR] Database - inicon\n' +
                  'Config: ', config.get_host(), config.get_port(), config.get_user(), config.get_pass(), config.get_database_name() +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            sys.exit

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