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
        conf = database.Config()
        conf = conf.get()
        try:
            self.connection = pymysql.connect(host = conf['ip'],
                                            port = conf['port'],
                                            user = conf['user'],
                                            password = conf['pass'],
                                            db = conf['name'],)
            self.cursor = self.connection.cursor()
            return self.cursor

        except pymysql.Error as Error:
            print('[ERROR] Database - inicon\n' +
                'Config: ',conf['ip'],conf['pass'],conf['user'],conf['pass'],conf['name'] +
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
