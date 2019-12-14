import os
import sys

import dataSource
from core.server_config import Config
from core.console import Console
from core.logging_handler import Logging,bcolors

from login.login_server import LoginServer
from exchange.exchange_server import ExchangeServer

def main():
    #  ======================================================
    #  start message
    log = Logging()
    console = Console()
    console.clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - Logon Server   |", 31*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    # ======================================================
    # data tests

    config = Config()
    config.initialize()

    log.info('Connection Test...')
    database = dataSource.Database()
    if database.get_connection():
        log.info('Connection Successfully')
    else:
        log.warning('Connection ERROR')
        sys.exit(0)

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
    print(58*"-")

    LoginServer().start(config.get_login_ip(), config.get_login_port())

    ExchangeServer().start(config.get_exchange_ip(), config.get_exchange_port())

    # ======================================================

if __name__ == '__main__':
    main()
