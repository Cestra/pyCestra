import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class Mapdata(DAO):

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
                cursor.execute('SELECT * FROM maps;')
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
