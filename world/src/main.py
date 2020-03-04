import os
import time

from core.logging_handler import Logging, bcolors
from core.server_config import Config
from exchange.exchange_client import ExchangeClient
from game.game_server import GameServer


class Main:

    def __init__(self):
        self.log = Logging()
        self.config = Config()

    def start(self):
        #  ======================================================
        #  start message

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
        exClient.initialize(self.config.get_exchange_ip(), self.config.get_exchange_port())

        time.sleep(3)
        # exClient.send('SS0')

        # self.log.debug('Game Server Start')
        # GameServer().initialize(exClient, self.config.get_world_ip(), self.config.get_world_port())

def main():
  Main().start()

if __name__== "__main__":
  main()
