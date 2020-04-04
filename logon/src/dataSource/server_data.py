'''
pyCestra - Open Source MMO Framework
Copyright (C) 2020 pyCestra Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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