import pymysql

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class PlayerData(DAO):

    def __init__(self):
        self.log = Logging()

    def load(self):
            '''
            DataFrame:
            
            '''
            self.Datasource = []
            connection = dataSource.Database().get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM players;')
                data = cursor.fetchall()
                for row in data:
                    Rows = [row]
                    self.Datasource.append(Rows)
            except pymysql.Error as Error:
                self.log.warning('player_data.py - Can\'t load table players' + Error)
                cursor.close()
                connection.close()
            finally:
                cursor.close()
                connection.close()
                # self.log.debug('cursor.close, connection.close')

    # Use databank player ID to find the right player
    def get_from_id(self, idwis):
        if not idwis == 0:
            player = idwis - 1
            return self.Datasource[player]
        else:
            self.log.warning('player_data.py - Can\'t load player id 0')
