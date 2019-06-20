import pymysql.cursors
from Config import Config

class Database():

    def __init__(self):
        pass

    def InitializeConnection(self):

        conf = Config().getDatafromLogonServerDatabase()
        if conf:
            pass
        else:
            print("Die logon.conf konnte NICHT erfolgreich ausgelesen werden")
            # Das ist ein default für die Config da die CMD nicht die logon.conf findet
            # self.conf = ['127.0.0.1', 3306, 'root', 'fabio312', 'cestra_game']

        try:
            connection = pymysql.connect(host = conf[0],
                                        port = conf[1],
                                        user = conf[2],
                                        password = conf[3],
                                        db = conf[4],)
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