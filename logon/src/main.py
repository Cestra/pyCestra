import sys
import time

import dataSource
from core.console import Console
from core.logging_handler import Logging, bcolors
from core.server_config import Config
from exchange.exchange_server import ExchangeServer
from login.login_server import LoginServer


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
    # print(serverData.get_from_id(1))

    playerData = dataSource.PlayerData()
    playerData.load()
    log.info('PlayerData were loaded')
    # print(playerData.get_from_id(1))

    accountData = dataSource.AccountData()
    accountData.load()
    log.info('AccountData were loaded')
    # print(accountData.get_from_id(1))

    # ======================================================
    # socket tests

    print(58*'-')

    game_client_dic = {}
    host_list_dic = {}

    LoginServer().start(config.get_login_ip(), config.get_login_port(), game_client_dic)

    ExchangeServer().start(config.get_exchange_ip(), config.get_exchange_port(), host_list_dic)

    while True:
        time.sleep(15)
        log.warning('---- game_client_dic ----')
        for x in game_client_dic:
            log.warning(str(x))
        log.warning('-------------------------')
        log.warning('---- host_list_dic ------')
        for x in host_list_dic:
            log.warning(str(x))
        log.warning('-------------------------')

    print('Test vorbei')

    # ======================================================

if __name__ == '__main__':
    main()
