import os
import time

from core.logging_handler import Logging, bcolors
from core.server_config import Config
from exchange.exchange_client import ExchangeClient
from game.game_server import GameServer

def main():
    #  ======================================================
    #  start message

    log = Logging()
    config = Config()

    def clear(): return os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - World Server   |", 31*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    #  ======================================================
    #  exchange client test

    exClient = ExchangeClient()
    exClient.initialize(config.get_exchange_ip(), config.get_exchange_port())
    # time.sleep(3)
    # exClient.send('SS0')

    log.debug('Game Server Start')
    GameServer().initialize(config.get_world_ip(), config.get_world_port())

if __name__ == '__main__':
    main()
