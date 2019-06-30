import pymysql.cursors

from Config import Config


class Database:
    '''
    ALWAYS close the Instans to close the Connection
    '''

    def __init__(self):
        # print("1. Database __init__")
        pass

    def __del__(self):
        # print("2. __del__")
        # self.connection.close()
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
            self.connection = pymysql.connect(host = conf[0],
                                        port = conf[1],
                                        user = conf[2],
                                        password = conf[3],
                                        db = conf[4],)
            self.cursor = self.connection.cursor()

            # TODO Wir sind grade hier und versuchen immer noch du testen ob alle connection
            # und cursor geschlossen werden! AccountData und ServerData sind auch nicht nicht
            # angepasst.
            #
            # if self.connection.open:
            #     print("OPEN")
            #     self.connection.close()
            #
            # TODO das hier über mir geht durch und verhindert eine verbindung, so wie es sein
            # sollte. Aber ich kann halt immer noch nur in der Funktion InitializeConnection nur
            # dir Verbindung benenden. außer halt geht es nicht.

            return self.cursor

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
            # cursor.Database().close()  TODO 1.Ist alt   2.Geht nicht

        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
        return False

'''
# ======================================
mySQLTest = Database()

def DatabaseTest():
    if mySQLTest.testConnection():
        print("Datenbank Connection Test Erfolgreich")
    else:
        print("Datanbank nicht gefunden!") 

DatabaseTest()
del mySQLTest
# ======================================
'''