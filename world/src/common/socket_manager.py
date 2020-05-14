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
import random

from common.name_generator import NameGenerator

from core.logging_handler import Logging


class SocketManager:

    def __init__(self, gameClient):
        self.log = Logging()
        self.nameGenerator = NameGenerator() # "world.join()" should quake it
        self.gameClient = gameClient
    
    def send(self, packet, name):
        __msg = bytes(packet + '\x00', 'utf-8')
        self.gameClient.get_session().send(__msg)
        self.log.debug('[{}][ACC:{}][SEND->] ({}) {}'.format(str(self.gameClient.get_addr()[0]),
                                                        str('X'),
                                                        name,
                                                        str(packet)))

    def GAME_SEND_HELLOGAME_PACKET(self):
        __name = 'GAME_SEND_HELLOGAME_PACKET'
        __packet = 'HG'
        self.send(__packet, __name)

    def GAME_SEND_ATTRIBUTE_FAILED(self):
        __name = 'GAME_SEND_ATTRIBUTE_FAILED'
        __packet = 'ATE'
        self.send(__packet, __name)

    def GAME_SEND_ATTRIBUTE_SUCCESS(self):
        __name = 'GAME_SEND_ATTRIBUTE_SUCCESS'
        __packet = 'ATK0'
        self.send(__packet, __name)

    def GAME_SEND_AV0(self):
        __name = 'GAME_SEND_AV0'
        __packet = 'AV0'
        self.send(__packet, __name)
    
    def MULTI_SEND_Af_PACKET(self, position, totalAbo, totalNonAbo, subscribe, queueID):
        __name = 'MULTI_SEND_Af_PACKET'
        __packet = ('Af{}|{}|{}|{}|{}'.format(str(position),
                                            str(totalAbo),
                                            str(totalNonAbo),
                                            str(subscribe),
                                            str(queueID)))
        self.send(__packet, __name)

    def GAME_SEND_PLAYER_LIST(self, sub, chrNum, palyerList):
        # ALK55751880000|1|1;pyCestra;1;80;-1;-1;-1;bc,96b,306,2593,2341;0;1;0;0;
        playerStr = ''
        for position, player in palyerList.items():
            string = ('|{};{};{};{};{};{};{};{},{},{},'
                       '{},{};{};{};0;0;'.format(str(position), # player display position ;
                                                player.get_name(), # player name ;
                                                str(player.get_level()), # player level ;
                                                player.get_gfx(), # gfx ID ;
                                                player.get_color1(), # color 1 in hex ;
                                                player.get_color2(), # color 2 in hex ;
                                                player.get_color3(), # color 3 in hex ;
                                                '', # weapon ID in hex ,
                                                '', # hat ID in hex ,
                                                '', # cape ID in hex ,
                                                '', # pet ID in hex ,
                                                '', # shield ID in hex ;
                                                '0', # isShowSeller 0 ;
                                                '1',)) # server ID ;
            playerStr += string
        __name = 'GAME_SEND_PLAYER_LIST'
        __packet = 'ALK{}|{}{}'.format(str(sub),str(chrNum),playerStr)
        self.send(__packet, __name)

    def REALM_SEND_REQUIRED_APK(self):
        __name = 'GAME_SEND_APK'
        __packet = 'APK'
        __chName = self.nameGenerator.get_name()
        self.send(__packet + __chName, __name)

    def GAME_SEND_NAME_ALREADY_EXIST(self):
        __name = 'GAME_SEND_NAME_ALREADY_EXIST'
        __packet = 'AAEa'
        self.send(__packet, __name)

    def GAME_SEND_CREATE_FAILED(self):
        __name = 'GAME_SEND_CREATE_FAILED'
        __packet = 'AAEF'
        self.send(__packet, __name)
    
    def GAME_SEND_CREATE_PERSO_FULL(self):
        __name = 'GAME_SEND_CREATE_PERSO_FULL'
        __packet = 'AAEf'
        self.send(__packet, __name)

    def GAME_SEND_CREATE_OK(self):
        __name = 'GAME_SEND_CREATE_OK'
        __packet = 'AAK'
        self.send(__packet, __name)

    def GAME_SEND_cMK_PACKET_TO_MAP(self):
        __name = 'GAME_SEND_cMK_PACKET_TO_MAP'
        # cMK" + suffix + "|" + guid + "|" + name + "|" + msg
        __packet = 'cMK'
        self.send(__packet, __name)

    def GAME_SEND_PERSO_SELECTION_FAILED(self):
        __name = 'GAME_SEND_PERSO_SELECTION_FAILED'
        __packet = 'ASE'
        self.send(__packet, __name)
    
    def GAME_SEND_DELETE_PERSO_FAILED(self):
        __name = 'GAME_SEND_DELETE_PERSO_FAILED'
        __packet = 'ADE'
        self.send(__packet, __name)