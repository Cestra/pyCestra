import os
import sys

import dataSource
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

    # ======================================================
    # Socket Tests

    '''
    PacketHandler().test_socket()
    '''

    # ======================================================
    # SQL Tests

    # only use if you need the config in main again
    # config = Config()
    # config.initialize()

    database = dataSource.Database()
    if database.getConnection():
        print('Connection Successfully')
    else:
        print('Connection ERROR')

    # serverData = dataSource.ServerData()
    # serverData = serverData.load()

    playerData = dataSource.PlayerData()
    playerData.load()
    print(playerData.get_from_id(0))
    # print(playerData.get())

    # ======================================================
