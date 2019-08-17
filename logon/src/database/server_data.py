import pymysql.cursors
# from DAO import DAO


# TODO vererbung test / auch wenn FROM oben angezeigt wird, geht es
class ServerData():

    def single_load(self, val):
        id = str(val)
        #try:
        cursor.execute("SELECT * FROM servers WHERE id = " + id)
        self.__data = cursor.fetchone()
        print(self.__data)
        '''
        except:
            print("[Error] @ ServerData.py - Can't load table servers")
            # TODO Hier muss noch geschlossen werden!!!
        '''

# TODO Oben wo cursor.execute("SEL... muss ein get_data von DAO hin