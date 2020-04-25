'''
pyCestra - Open Source MMO Framework
Copyright (C) 2020 pyCestra Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os
import sys
import time

import dataSource
from core.logging_handler import Logging, bcolors
from core.server_config import Config
from dataSource.database import Database
from exchange.exchange_client import ExchangeClient
from game.game_server import GameServer
from game.world.world import World


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
            welmsg = [58*'─', '|  0.01  |' + 12*' ' +
                'pyCestra -  World Server'+ 11*' ' + '|', 58*"─"]
            for x in welmsg:
                print(bcolors.blue + x + bcolors.cend)
        wel()

        #  ======================================================
        #  connection test

        self.log.info('Connection Test...')
        database = dataSource.Database()
        if database.get_connection():
            self.log.info('Connection Successfully')
        else:
            self.log.warning('Connection ERROR')
            sys.exit(0)

        #  ======================================================
        #  world class test
             
        world = World().createWorld()

        #  ======================================================
        #  exchange client test

        # exchangeTransferList = []
        # exClient = ExchangeClient()
        # exClient.initialize(self.config.get_exchange_ip(),
        #                     self.config.get_exchange_port(),
        #                     exchangeTransferList)

        # time.sleep(1)

        # self.log.debug('Game Server Start')
        # # GameServer().initialize(exClient, self.config.get_world_ip(), self.config.get_world_port())
        # GameServer().initialize(self.config.get_world_ip(),
        #                         self.config.get_world_port(),
        #                         exchangeTransferList)

def main():
  Main().start()

if __name__== "__main__":
  main()
