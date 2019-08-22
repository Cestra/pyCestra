import pymysql.cursors

import dataSource
from dataSource.DAO import DAO


class PlayerData(DAO):

    def load(self):
            '''
            DataFrame:
            
            '''
            self.Datasource = []
            connection = dataSource.Database().getConnection()
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM players;")
                data = cursor.fetchall()
                for row in data:
                    Rows = [row]
                    self.Datasource.append(Rows)
            except:
                print("[Error] @ server_data.py - Can't load table players")
                cursor.close()
                connection.close()
            finally:
                cursor.close()
                connection.close()
                print('[DEBUG] cursor.close, connection.close')

    # Use databank player ID to find the right player
    def get_from_id(self, idwis):
        if not idwis == 0:
            player = idwis - 1
            return self.Datasource[player]
        else:
            print("[Error] @ server_data.py - Can't load Player id 0 ")
    
    def set(self, ip):
        pass