import pymysql.cursors

import database


class Database:
    '''
    ALWAYS close the Instans to close the Connection
    '''

    def __init__(self):
        # print("1. __init__")
        pass

    def __del__(self):
        # print("2. __del__")
        # self.connection.close()
        pass

    # Initialize Connection
    def inicon(self):
        config = database.Config()
        config.initialize()
        try:
            self.connection = pymysql.connect(host = config.getHost(),
                                            port = config.getPort(),
                                            user = config.getUser(),
                                            password = config.getPass(),
                                            db = config.getDatabaseName())
            self.cursor = self.connection.cursor()
            return self.cursor

        except pymysql.Error as Error:
            print('[ERROR] Database - inicon\n' +
                'Config: ',config.getHost(),config.getPort(),config.getUser(),config.getPass(),config.getDatabaseName() +
                '\nDatabase - inicon - Something went wrong: {}'.format(Error))
            return False

    def testConnection(self):
        try:
            cursor = Database().inicon()
            if cursor:
                cursor.execute('SELECT VERSION()')
                results = cursor.fetchone()
                if results:
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
