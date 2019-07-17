import database


class ServerData:

    def __init__(self, val):
        id = str(val)
        cursor = database.Database().inicon()
        try:
            cursor.execute("SELECT * FROM players WHERE id = " + id)
            self.__data = cursor.fetchone()
        except:
            print("Error @ ServerData.py -  __init__")
            # TODO Hier muss noch geschlossen werden!!! 
    
    def get(self):
        return self.__data
    
    def set(self, ip):
        pass