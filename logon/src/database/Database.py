import pymysql.cursors
from src.Config import Config

class Database:

    def initializeConnection(self):
        con = Config().getData_LogonServerDatabase()
        try:
            connection = pymysql.connect(host = con['ip'],
                                        port = con['port'],
                                        user = con['user'],
                                        password = con['passwo'],
                                        db = con['name'],
                                        cursorclass = pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            return cursor
        
        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
            return("Connection Error")

    def testConnection(self):
        # global initializeConnection()
        try:
            cursor = Database().initializeConnection()
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