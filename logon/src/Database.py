import pymysql.cursors
import ConfigParser

def getConfig(self):
    config_file = "logon.conf"

def initializeConnection():
    try:
        connection = pymysql.connect(host="127.0.0.1",
                                    user="root",
                                    password="fabio312",
                                    db="cestra_game",
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        return cursor
    
    except pymysql.Error as Error:
        print("Something went wrong: {}".format(Error))
        return("Connection Error")

def testConnetcion():
    try:
        cursor = initializeConnection()
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

# ======================================
if testConnetcion() == True:
    print("testConnetcion Erfolgreich")
else:
    print("GEHT NICHT")
# ======================================

