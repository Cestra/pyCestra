import os

from core.logging_handler import Logging, bcolors
from core.server_config import Config
from exchange.exchange_client import ExchangeClient
from game.game_server import GameServer

def main():
    #  ======================================================
    #  start message

    log = Logging()

    def clear(): return os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - World Server   |", 31*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    #  ======================================================
    #  exchange client test

    log.debug('Client Start')
    ExchangeClient().test()

    # GameServer().initialize('127.0.0.1', 5555)

if __name__ == '__main__':
    main()
