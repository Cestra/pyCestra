'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

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

# https://dev.mysql.com/downloads/connector/python/
# pip install mysql-connector-python

import mysql.connector

from core.logging_handler import Logging
from core.server_config import Config


class Database():
    '''
    INFO: ALWAYS close the Instans to close the Connection
    '''
    def __init__(self):
        self.log = Logging()
        self.log.debug('Database instance has been created')

    #initialize_connection
    def get_connection(self):
        config = Config()
        config.initialize()
        try:
            connection = mysql.connector.connect(host=config.get_host(),
                                        port=config.get_port(),
                                        user=config.get_user(),
                                        password=config.get_pass(),
                                        db=config.get_database_name(),
                                        auth_plugin='mysql_native_password')
            return connection

        except mysql.connector.Error as Error:
            self.log.warning('Database - initialize_connection\n' +
                            'Config: '+ str(config.get_host()) + ' - ' +
                            str(config.get_port()) + ' - ' +
                            str(config.get_user()) + ' - ' +
                            str(config.get_pass()) + ' - ' +
                            str(config.get_database_name()) +
                            '\nDatabase - inicon - Something went wrong: {}'.format(str(Error)))
            return False
