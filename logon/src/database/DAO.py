import pymysql.cursors


class DAO:

    def get_data(self, query):
        try:
                if not query.endswith(';'):
                    query += ";"
                print(query)
        except:
            pass


s = DAO()
s.get_data("Ich bin ein String")