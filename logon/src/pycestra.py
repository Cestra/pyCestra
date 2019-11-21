import os
import sys

import dataSource
from core.server_config import Config
from core.console import Console
from core.logging_handler import Logging,bcolors

# from packet_handler import PacketHandler
from login.login_server import LoginServer

class main():

    global maina
    maina = 10000
    maina + 1
    #  ======================================================
    #  start message
    log = Logging()
    console = Console()

    # def clear(): return os.system('cls')
    # clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - Logon Server   |", 31*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    # ======================================================
    # data tests

    # only use if you need the config in main again
    config = Config()
    config.initialize()

    log.info('Connection Test...')
    database = dataSource.Database()
    if database.get_connection():
        log.info('Connection Successfully')
    else:
        log.info('Connection ERROR')
        sys.exit()

    serverData = dataSource.ServerData()
    serverData.load()
    log.info('ServerData were loaded')
    # # print(serverData.get_from_id(1))

    playerData = dataSource.PlayerData()
    playerData.load()
    log.info('PlayerData were loaded')
    # # print(playerData.get_from_id(1))

    accountData = dataSource.AccountData()
    accountData.load()
    log.info('AccountData were loaded')
    # # print(accountData.get_from_id(1))

    # ======================================================
    # socket tests

    LoginServer().start(config.get_login_ip(), config.get_login_port())

    # ======================================================
 