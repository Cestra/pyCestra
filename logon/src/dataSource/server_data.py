import pymysql.cursors

import dataSource
from dataSource.DAO import DAO


class ServerData(DAO):

    def load(self):
        '''
        DataFrame:
        [['Demo', 'demo', 0, 0, 1494344975925], ['Jiva', 'jiv', 0, 0, 1494344975925]]
        '''
        self.Datasource = []
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM servers;")
            data = cursor.fetchall()
            for row in data:
                Rows = [row]
                self.Datasource.append(Rows)
        except:
            print("[Error] @ server_data.py - Can't load table servers")
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()
            print('[DEBUG] cursor.close, connection.close')
    
    # Use databank server ID to find the right server
    def get_from_id(self, idwis):
        if not idwis == 0:
            player = idwis - 1
            return self.Datasource[player]
        else:
            print("[Error] @ player_data.py - Can't load server id 0 ")
