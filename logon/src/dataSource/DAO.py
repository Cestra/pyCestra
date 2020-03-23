import dataSource


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
            self.log.warning('DAO.py - Can\'t load:')
            self.log.warning(query)
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()

    def update_data(self, query):
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except:
            self.log.warning('DAO.py - Can\'t update the Database')
            self.log.warning(query)
        finally:
            cursor.close()
            connection.close()

# name = 'admin'
# data = DAO().get_data("SELECT * FROM accounts WHERE account = '" + str(name) + "';")
