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
from client.player import Player
from core.logging_handler import Logging
from dataSource.players_data import PlayersData
from constant import Constant

class World:

    def __init__(self):
        self.log = Logging()
        self.constant = Constant()

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

    def get_players_by_accid(self, accId):
        __playerList = []
        for player in self.playersData:
            if player.get_account_id() == accId:
                __playerList.append(player)
        return __playerList
    
    def create_player(self, accId, name, pClass, sex, color1, color2, color3):
        playerID = 0
        for player in self.playersData:
            if player.get_id() > playerID:
                playerID = player.get_id()
        playerID = playerID + 1

        startMapCellList = self.constant.get_start_map_incarnam(pClass)
        __player = Player(playerID, name, accId, -1, # id, name, account, group,
                        sex, pClass, color1, color2, color3, # sexe, pClass, color1-3,
                        0, 1, '', 10000, 1, # kamas, spellboost, capital, energy, level,
                        #0, 100, pClass * 10 + sex, # xp, size, gfx,
                        0, 100, (pClass * 10 + sex), # xp, size, gfx,
                        0, 0, 0, 0,# alignement, honor, deshonor, alvl,
                        [0,0,0,0,0,0], 1, 0, # stats(list), seeFriend, seeAlign,
                        0, '*#%!pi$:?', startMapCellList[0], # seeSeller, channel, map,
                        startMapCellList[1], 100, # cell, pdvper,
                        '141;', # spells <-- TODO placeholder
                        '', '', # objets, storeObjets,
                        str(startMapCellList[0]) + ':' + str(startMapCellList[1]), # savepos
                        '', '', 0, # zaaps, jobs, mountxpgive, 
                        0, 0, '0;0', # title, wife, morphMode,
                        '', 0, 1, # emotes, prison, server, <-- TODO placeholder
                        True, '', # logged allTitle
                        '118,0;119,0;123,0;124,0;125,0;126,0', 0, 0,) # parcho, timeDeblo, noall
        self.playersData.append(__player)
