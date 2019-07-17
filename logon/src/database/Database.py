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
        print(type(conf))
        try:
            self.connection = pymysql.connect(host = conf['ip'],
                                            port = conf['pass'],
                                            user = conf['user'],
                                            password = conf['pass'],
                                            db = conf['name'],)
            self.cursor = self.connection.cursor()
            return self.cursor

        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
            return("Connection Error")

    def testConnection(self):
        try:
            cursor = Database().inicon()
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            if results:
                return True
            else:
                return False
            # cursor.Database().close()  TODO 1.Ist alt   2.Geht nicht

        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
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
