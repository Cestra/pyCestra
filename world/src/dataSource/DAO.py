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

import dataSource
import mysql.connector
from core.logging_handler import Logging


class DAO:

    def __init__(self):
        self.log = Logging()
        self.connection = dataSource.Database().get_connection()
        self.cursor = self.connection.cursor()

    def get_data(self, query):
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            if not query.endswith(';'):
                    query += ";"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Exception as e:
            self.log.warning('DAO.py - Can\'t load: \n{}\n{}'.format(query,str(e)))
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()

    def multi_update_data(self, query):
        '''
        This function does not end the connection after use
        '''
        try:
            if not query.endswith(';'):
                    query += ";"
            self.cursor.execute(query)
        except pymysql.Error as Error:
            self.log.warning('DAO.py - update_data - Can\'t update the Database\n{}\n{}'.format(str(Error),query))
