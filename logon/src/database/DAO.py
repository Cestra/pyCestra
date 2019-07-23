import pymysql.cursors


class DAO:

    def getData(self, query):
        try:
                if not query.endswith(';'):
                    query += ";"
                print(query)
        except:
            pass


s = DAO()
s.getData("Ich bin ein String")