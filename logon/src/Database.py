import pymysql.cursors
from Config import Config

class Database():

    def InitializeConnection(self):
        conf = Config().getDatafromLogonServerDatabase()
        try:
            connection = pymysql.connect(host = conf['ip'],
                                        port = conf['port'],
                                        user = conf['user'],
                                        password = conf['passwo'],
                                        db = conf['name'],
                                        cursorclass = pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            return cursor

        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
            return("Connection Error")

    def testConnection(self):
        try:
            cursor = Database().InitializeConnection()
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            if results:
                return True
            else:
                return False
            cursor.close()

        except pymysql.Error:
            print("ERROR IN CONNECTION")
        return False

'''
# ======================================
if Database().testConnection() == True:
    print("testConnetcion Erfolgreich")
else:
    print("GEHT NICHT")
# ======================================
'''