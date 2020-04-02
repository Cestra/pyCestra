import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class MapData(DAO):

    def __init__(self):
        self.log = Logging()

    def load(self):
        '''
        DataFrame:

        '''
        self.dataSource = []
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT * FROM accounts;')
            data = cursor.fetchall()
            for row in data:
                self.dataSource.append(row)
        except Exception as Error:
            self.log.warning(' account_data.py - Can\'t load table accounts')
            self.log.warning(str(Error))
        finally:
            cursor.close()
            connection.close()

    def get_map_data(self):
        print('bin ich hier ?????')
        return self.dataSource
