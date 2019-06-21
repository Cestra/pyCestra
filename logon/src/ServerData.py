import pymysql.cursors

from Database import Database

class ServerData:

    def __init__(self, val):
        self.cursor = Database().InitializeConnection()
        id = str(val)
        try:
            self.cursor.execute("SELECT * FROM servers WHERE id = " + id)
            self.__data = self.cursor.fetchone()
        except pymysql.Error as Error:
            print("Something went wrong: {}".format(Error))
        self.cursor.close()
    
    def get(self):
        return self.__data
    
    def set(self, ip):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

test = ServerData(1).get()
print(test)