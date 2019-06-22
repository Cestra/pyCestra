import pymysql.cursors

from Database import Database

class AccountData:

    def __init__(self, val):
        self.cursor = Database().InitializeConnection()
        id = str(val)
        try:
            self.cursor.execute("SELECT * FROM accounts WHERE guid = " + id)
            self.__data = self.cursor.fetchone()
        except:
            print("Error @ AccountData.py -  __init__")
            self.cursor.Database().close()
    
    def get(self):
        return self.__data
    
    def set(self, ip):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

# test = AccountData(1).get()
# print(test)