import pymysql

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class ServerData(DAO):

    def __init__(self):
        self.log = Logging()

    def load(self):
        '''
        DataFrame:
        id, name, key, population, isSubscriberServer
        ['1','Demo', 'demo', 0, 0,]

        relevant data:
        id, key, population, isSubscriberServer
        ['1', 'key', 'population', 'isSubscriberServer']
        '''
        self.Datasource = []
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT * FROM servers;')
            data = cursor.fetchall()
            for result in data:
                # only relevant data is saved
                row = {'id':result['id'],
                        'key':result['key'],
                        'population':result['population'],
                        'isSubscriberServer':result['isSubscriberServer'],}
                self.Datasource.append(row)
        except pymysql.Error as Error:
            self.log.warning('server_data.py - Can\'t load table servers - ')
            self.log.warning(str(Error))
        finally:
            cursor.close()
            connection.close()

    # Use databank server ID to find the right server
    def get_from_id(self, idwis):
        if not idwis == 0:
            player = idwis - 1
            return self.Datasource[player]
        else:
            self.log.warning('player_data.py - Can\'t load server id 0')
