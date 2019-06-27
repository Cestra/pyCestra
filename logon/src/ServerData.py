from Database import Database

class ServerData:

    def __init__(self, val):
        cursor = Database().InitializeConnection()
        id = str(val)
        try:
            cursor.execute("SELECT * FROM servers WHERE id = " + id)
            self.__data = cursor.fetchone()
        except:
            print("Error @ ServerData.py -  __init__")
            cursor.Database().close()
    
    def get(self):
        return self.__data
    
    def set(self, ip):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

# test = ServerData(1).get()
# print(test)