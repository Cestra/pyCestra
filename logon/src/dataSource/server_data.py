import pymysql.cursors

import dataSource
from dataSource.DAO import DAO


class ServerData(DAO):

    def single_load(self, val):
        id = str(val)
        connection = dataSource.Database().getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM servers WHERE id = " + id)
            self.data = cursor.fetchone()
            # None Check:
            if self.data:
                return self.data
            else:
                return False
        except:
            print("[Error] @ DAO - ServerData - Can't load table servers")
            cursor.close()
            connection.close()

    def load(self):
        '''
        DataFrame:
        [['Demo', 'demo', 0, 0, 1494344975925], ['Jiva', 'jiv', 0, 0, 1494344975925]]
        '''
        Datasource = []
        connection = dataSource.Database().getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM servers;")
            data = cursor.fetchall()
            for row in data:
                Rows = [row[1], row[2], row[3], row[4], row[5]]
                Datasource.append(Rows)
        except:
            print("[Error] @ DAO - ServerData - Can't load table servers")
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()
            print('[DEBUG] cursor.close, connection.close')
            return Datasource
