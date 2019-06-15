import pymysql.cursors
import configparser

class Database:

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read('logon.conf')
        print(config.sections())
        # print(config['DEFAULT']['Logon_Database_Ip'])

    def initializeConnection(self):
        try:
            connection = pymysql.connect(host="127.0.0.1",
                                        port=3306,
                                        user="root",
                                        password="fabio312",
                                        db="cestra_game",
                                        cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            return cursor
        
        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
            return("Connection Error")

    def testConnetcion(self):
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

Database().getConfig()


'''
# ======================================
if Database().testConnetcion() == True:
    print("testConnetcion Erfolgreich")
else:
    print("GEHT NICHT")
# ======================================
'''