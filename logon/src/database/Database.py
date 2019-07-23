import sys

import pymysql.connections

import database


class Database:
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''

    def initializeData(self):
        pass

    def initializeConnection(self):
        config = database.Config()
        config.initialize()
        try:
            self.connection = pymysql.connect(host=config.getHost(),
                                              port=config.getPort(),
                                              user=config.getUser(),
                                              password=config.getPass(),
                                              db=config.getDatabaseName())
            self.cursor = self.connection.cursor()
            return True

        except pymysql.Error as Error:
            print('[ERROR] Database - inicon\n' +
                  'Config: ', config.getHost(), config.getPort(), config.getUser(), config.getPass(), config.getDatabaseName() +
                  '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            sys.exit
            return False

    def testConnection(self):
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
