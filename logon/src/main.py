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
        welmsg = [58*'─', '|  0.01  |' + 12*' ' + 
                'pyCestra - Logon Server'+ 12*' ' + '|', 58*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    # ======================================================
    # preload data

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

    accountData = dataSource.AccountData()
    accountData.load()
    log.info('AccountData were loaded')
    # print(accountData.get_from_id(1))

    ipbans = dataSource.IpBans().load()
    log.info('IP Bans were loaded')

    updateTime = 2

    databaseUpdateService = dataSource.DatabaseUpdateService().start(accountData.get_account_data(), updateTime)

    # ======================================================
    # socket tests

    print(58*'-')

    game_client_dic = {}
    host_list_dic = {}

    LoginServer().start(config.get_login_ip(), config.get_login_port(), game_client_dic, ipbans)

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

    # ======================================================

if __name__ == '__main__':
    main()
