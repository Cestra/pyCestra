from DAO import DAO

# TODO vererbung test / auch wenn FROM oben angezeigt wird, geht es
class ServerData(DAO):

    def __init__(self, val):
        id = str(val)
        cursor = 0
        try:
            cursor.execute("SELECT * FROM servers WHERE id = " + id)
            self.__data = cursor.fetchone()
        except:
            print("Error @ ServerData.py -  __init__")
            # TODO Hier muss noch geschlossen werden!!! 
    
    def get(self):
        return self.__data
    
    def set(self, ip):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

# test = ServerData(1).get()
# print(test)
# print(len(test))
