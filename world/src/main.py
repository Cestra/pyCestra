import os
import sys
import time

import dataSource
from core.logging_handler import Logging, bcolors
from core.server_config import Config
from exchange.exchange_client import ExchangeClient
from game.game_server import GameServer
from dataSource.database import Database
from dataSource.map_data import MapData


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

        # ======================================================
        # preload data

        # self.log.info('Connection Test...')
        # database = Database()
        # if database.get_connection():
        #     self.log.info('Connection Successfully')
        # else:
        #     self.log.warning('Connection ERROR')
        #     sys.exit(0)

        # test = MapData().pre_Load()
        

        #  ======================================================
        #  data test

        # self.log.info('Connection Test...')
        # database = dataSource.Database()
        # if database.get_connection():
        #     self.log.info('Connection Successfully')
        # else:
        #     self.log.warning('Connection ERROR')
        #     sys.exit(0)
        
        # mapdata = dataSource.MapData()
        # mapdata.load()
        #mapdatatest = mapdatatest.get_map_data()
        #print(mapdatatest)


        #  ======================================================
        #  exchange client test

        exClient = ExchangeClient()
        exClient.initialize(self.config.get_exchange_ip(), self.config.get_exchange_port())

        # time.sleep(3)

        # self.log.debug('Game Server Start')
        # GameServer().initialize(exClient, self.config.get_world_ip(), self.config.get_world_port())

def main():
  Main().start()

if __name__== "__main__":
  main()
