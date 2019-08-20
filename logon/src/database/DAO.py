import pymysql.cursors

from database.database import Database

global ServerData

class DAO:

    def get_data(self, query):
        try:
                if not query.endswith(';'):
                    query += ";"
                print(query)
        except:
            pass

    # is not in use anymore
    # super().none_check(self.data)
    def none_check(self, query):
        if query:
            return True
        else:
            return False

class ServerData(DAO):

    def single_load(self, val):
        id = str(val)
        connection = Database().getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM servers WHERE id = " + id)
            self.data = cursor.fetchone()
            if self.data:
                return self.data
            else:
                return False
        except:
            print("[Error] @ DAO - ServerData - Can't load table servers")
            # TODO CLOSE