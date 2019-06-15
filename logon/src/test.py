import pymysql.cursors

def map_crypt_places(mapid):
    try:
        connection = pymysql.connect(host="127.0.0.1",
                                    user="root",
                                    password="fabio312",
                                    db="cestra_game",
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute("SELECT places FROM cestra_game.maps WHERE id = " + mapid)

        try:
            MapData = cursor.fetchone()
            return(str(MapData["places"]))

        except:
            return("Unknown Map (except from map_crypt_places)")

        cursor.close()
        connection.close()

    except pymysql.Error as Error:
        print("Something went wrong: {}".format(Error))
        return("Connection Error")

# darf nicht gehen!
print(map_crypt_places("878"))
# muss gehen!
print(map_crypt_places("952"))