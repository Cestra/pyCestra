'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

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
        self.maps = {} # ID(int), MAP(object)

    def createWorld(self):
        self.log.info(35*'-')
        self.log.info('Creation of the world begins:')
        # --------------------------------------------------------------------
        # Players data are loading here
        self.playersData = dataSource.PlayersData()
        self.playersData.load_in_to_class()
        self.playersData = self.playersData.get_player_data()
        self.log.info(8*'-'+' Player were loaded '+7*'-')
        # --------------------------------------------------------------------
        # Maps data are loaded here
        __mapData = dataSource.MapData()
        __mapData.load_in_to_class()
        __mapData = __mapData.get_map_data()
        for __mapId, __mapObject in __mapData.items():
            self.add_map(__mapId, __mapObject)
        del __mapData, __mapId, __mapObject
        self.log.info(8*'-'+' Maps were loaded '+9*'-')

        self.log.info('The world-server has finished loading')
        self.log.info(35*'-')

    def add_map(self, id, mapObject):
        self.maps[id] = mapObject

    def get_map(self, id):
        return self.maps.get(id)

    def get_players(self):
        return self.playersData

    def get_players_by_accid(self, accId):
        __playerList = {}
        __position = 1
        for player in self.playersData:
            if player.get_account_id() == accId:
                __playerList[__position] = player
                __position += 1
        return __playerList
    
    def create_player(self, accId, name, pClass, sex, color1, color2, color3):
        __playerID = 0
        for player in self.playersData:
            if player.get_id() > __playerID:
                __playerID = player.get_id()
        __playerID = __playerID + 1

        __startMapCellList = self.constant.get_start_map_incarnam(pClass)
        player = Player(__playerID, name, accId, -1, # id, name, account, group,
                        sex, pClass, color1, color2, color3, # sexe, pClass, color1-3,
                        0, 1, '', 10000, 1, # kamas, spellboost, capital, energy, level,
                        #0, 100, pClass * 10 + sex, # xp, size, gfx,
                        0, 100, (pClass * 10 + sex), # xp, size, gfx,
                        0, 0, 0, 0,# alignement, honor, deshonor, alvl,
                        [0,0,0,0,0,0], 1, 0, # stats(list), seeFriend, seeAlign,
                        0, '*#$p^', __startMapCellList[0], # seeSeller, channel, map,
                        __startMapCellList[1], 100, # cell, pdvper,
                        '141;', # spells <-- TODO placeholder
                        '', '', # objets, storeObjets,
                        str(__startMapCellList[0]) + ':' + str(__startMapCellList[1]), # savepos
                        '', '', 0, # zaaps, jobs, mountxpgive, 
                        0, 0, '0;0', # title, wife, morphMode,
                        '', 0, 1, # emotes, prison, server, <-- TODO placeholder
                        True, '', # logged allTitle
                        '118,0;119,0;123,0;124,0;125,0;126,0', 0, 0,) # parcho, timeDeblo, noall
        del __startMapCellList
        self.playersData.append(player)
    
    def delete_player(self, __playerID):
        # TODO remove player from his guild
        # TODO remove all his objets
        # determination of the list position
        __listPosition = 0
        for player in self.playersData:
            if player.get_id() == __playerID:
                break
            else:
                __listPosition += 1
        # delete list entry (in self.playersData)
        del self.playersData[__listPosition]
