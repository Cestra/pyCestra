import pymysql

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO
from object.server import Server


class ServerData(DAO):

    def __init__(self):
        self.log = Logging()
        self.Datasource = []

    def load(self):
        '''
        DataFrame:
        id, name, key, population, isSubscriberServer
        ['1','Demo', 'demo', 0, 0,]

        relevant data:
        id, key, population, isSubscriberServer
        ['1', 'key', 'population', 'isSubscriberServer']
        '''
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT * FROM servers;')
            data = cursor.fetchall()
            for result in data:
                # only relevant data is saved
                server = Server(result['id'],
                                result['key'],
                                0,
                                result['population'],
                                result['isSubscriberServer'])
                
                self.Datasource.append(server)
        except pymysql.Error as Error:
            self.log.warning('server_data.py - Can\'t load table servers - ')
            self.log.warning(str(Error))
        finally:
            cursor.close()
            connection.close()

    def get_server_data(self):
        return self.Datasource