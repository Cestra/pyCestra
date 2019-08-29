import pymysql.cursors

import dataSource

# global ServerData

class DAO:

    def get_data(self, query):
        try:
                if not query.endswith(';'):
                    query += ";"
                print(query)
        except:
            pass
