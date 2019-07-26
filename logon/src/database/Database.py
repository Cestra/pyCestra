import sys

import pymysql.connections

import database


class Database:
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''

    def initialize_data(self):
        pass

    def initialize_connection(self):
        config = database.Config()
        config.initialize()
        try:
            self.connection = pymysql.connect(host=config.get_host(),
                                              port=config.get_port(),
                                              user=config.get_user(),
                                              password=config.get_pass(),
                                              db=config.get_database_name())
            self.cursor = self.connection.cursor()
            return True

        except pymysql.Error as Error:
            print('[ERROR] Database - inicon\n' +
                  'Config: ', config.get_host(), config.get_port(), config.get_user(), config.get_pass(), config.get_database_name() +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            sys.exit
            return False

    def test_connection(self):
        try:
            cursor = Database().inicon()
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


# ======================================
# mySQLTest = Database()

# def DatabaseTest():
#     if mySQLTest.testConnection():
#         print("Datenbank Connection Test Erfolgreich")
#     else:
#         print("Datanbank nicht gefunden!")

# DatabaseTest()
# del mySQLTest
# ======================================
