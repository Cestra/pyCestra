import pymysql.cursors

import dataSource

# global ServerData

class DAO:

    def get_data(self, query):
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            if not query.endswith(';'):
                    query += ";"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except:
            self.log.warning(' account_data.py - Can\'t load table accounts')
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()

# name = 'admin'
# data = DAO().get_data("SELECT * FROM accounts WHERE account = '" + str(name) + "';")
