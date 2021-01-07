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

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class AccountData(DAO):

    def __init__(self):
        self.log = Logging()
        self.Datasource = []

    def load(self):
            '''
            DataFrame:

            '''
            connection = dataSource.Database().get_connection()
            cursor = connection.cursor(dictionary=True)
            try:
                cursor.execute('SELECT * FROM accounts;')
                data = cursor.fetchall()
                for row in data:
                    self.Datasource.append(row)
            except Exception as Error:
                self.log.warning(' account_data.py - Can\'t load table accounts')
                self.log.warning(str(Error))
            finally:
                cursor.close()
                connection.close()

    def get_account_data(self):
        return self.Datasource

    def single_update(self, acc_id, valueTyp, value):
        '''
        acc_id
        valueTyp = Column name as in the database
        value

        example:
        update(1,'logged','1')
        '''
        data = 'UPDATE `accounts` SET `{}` = \'{}\' WHERE (`id` = \'{}\');'.format(str(valueTyp),str(value),str(acc_id))
        super().update_data(data)

    # Use databank account ID to find the right account
    def get_from_id(self, idwis):
        if not idwis == 0:
            account = idwis - 1
            return self.Datasource[account]
        else:
            self.log.warning('account_data.py - Can\'t load account id 0')
