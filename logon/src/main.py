import os
import sys

from database.database import Database

from database.DAO import DAO,ServerData
# from database.server_data import ServerData

from core.config import Config
# from PacketHandler import PacketHandler

if __name__ == "__main__":

    #  ======================================================
    #  start message

    def clear(): return os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - Logon Server   |", 31*"─"]
        for x in welmsg:
            print(x)
    wel()

    #  ======================================================
    #  Socket Tests

    '''
    PacketHandler().test_socket()
    '''

    #  ======================================================

    # only use if you need the config in main again
    # config = Config()
    # config.initialize()

    database = Database()
    if database.getConnection():
        print('Connection Successfully')
    else:
        print('Connection ERROR')

    serverData = ServerData()
    serverData = serverData.load()

    #  ======================================================