import database


class AccountData:

    def __init__(self, val):
        id = str(val)
        cursor = database.Database().inicon()
        try:
            cursor.execute("SELECT * FROM accounts WHERE guid = " + id)
            self.__data = cursor.fetchone()
        except:
            print("Except @ AccountData.py -  __init__")
            # TODO Hier muss noch geschlossen werden!!!

    def get(self):
        return self.__data
    
    def set(self, ip, val, row):
        # Account Daten zu ändern ist mir noch zu schwer
        # Um an die daten zu kommen self.__data
        pass

# test = AccountData(1).get()
# print(test)
