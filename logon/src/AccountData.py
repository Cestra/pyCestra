from Database import Database

class AccountData:

    def __init__(self, val):
        id = str(val)
        cursor = Database().InitializeConnection()
        try:
            cursor.execute("SELECT * FROM accounts WHERE guid = " + id)
            self.__data = cursor.fetchone()
        except:
            print("Error @ AccountData.py -  __init__")
            cursor.Database().close()
    
    def get(self):
        return self.__data
    
    def set(self, ip, val):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

# test = AccountData(1).get()
# print(test)