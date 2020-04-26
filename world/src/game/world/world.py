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

import dataSource
from core.logging_handler import Logging
from dataSource.players_data import PlayersData


class World:

    def __init__(self):
        self.log = Logging()

    def createWorld(self):
        self.log.info(35*'-')
        self.log.info('Creation of the world begins:')

        self.playersData = dataSource.PlayersData()
        self.playersData.load_in_to_class()
        self.playersData = self.playersData.get_player_data()
        self.log.info('Player were loaded')

        self.log.info('The world-server has finished loading')
        self.log.info(35*'-')

    def get_players(self):
        return self.playersData

    def get_players_by_accid(self, accid):
        __playerList = []
        for player in self.playersData:
            if player.get_id() == accid:
                __playerList.append(player)
        return __playerList
