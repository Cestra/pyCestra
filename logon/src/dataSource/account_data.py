import typing

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO
# from object.account import Account


class AccountData(DAO):

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
                cursor.execute('SELECT * FROM accounts;')
                data = cursor.fetchall()
                for row in data:
                    self.Datasource.append(row)
            except:
                self.log.warning(' account_data.py - Can\'t load table accounts')
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
        '''
        preloading necessary!
        '''
        if not idwis == 0:
            account = idwis - 1
            return self.Datasource[account]
        else:
            self.log.warning('account_data.py - Can\'t load account id 0')
