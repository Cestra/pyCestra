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

import threading

from core.logging_handler import Logging
from game.game_client import GameClient
from common.socket_manager import SocketManager


class GameHandler:

    def __init__(self, socket, addr, exchangeTransferList, world):
        self.log = Logging()
        self.world = world
        self.socketManager = SocketManager()
        gameClient = GameClient(socket, addr)
        self.socketManager.GAME_SEND_HELLOGAME_PACKET(gameClient)
        self.loop(gameClient, exchangeTransferList)

    def loop(self, gameClient, exchangeTransferList):
        while True:
            data = gameClient.get_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n\x00', '[n][x00]')
            self.log.debug('[{}][ACC:{}][<-RECV] {}'.format(str(gameClient.get_addr()[0]),
                                                            str('X'),
                                                            str(packetLog)))
            if not data:
                self.log.debug('[{}][ACC:{}] PacketLoop no data'.format(str(gameClient.get_addr()[0]),
                                                                str('X')))
                gameClient.kick()
                break
            multiPacket = packet.split("\n\x00")
            if len(multiPacket) > 2:
                for p in multiPacket:
                    if not p == '':
                        self.parse(gameClient, p, exchangeTransferList)
            else:
                self.parse(gameClient, packet.replace('\n\x00', ''), exchangeTransferList)

# --------------------------------------------------------------------
# MAIN PARSE

    def parse(self, gameClient, packet, exchangeTransferList):
        if packet[0] == 'A':
            self.log.warning('parse_account_packet')
            self.parse_account_packet(gameClient, packet, exchangeTransferList)
            return
        elif packet[0] == 'B':
            self.log.warning('parseBasicsPacket')
            return
        elif packet[0] == 'C':
            self.log.warning('parseConquestPacket')
            return
        elif packet[0] == 'c':
            self.log.warning('parseChanelPacket')
            return
        elif packet[0] == 'D':
            self.log.warning('parseDialogPacket')
            return
        elif packet[0] == 'd':
            self.log.warning('parseDocumentPacket')
            return
        elif packet[0] == 'E':
            self.log.warning('parseExchangePacket')
            return
        elif packet[0] == 'e':
            self.log.warning('parseEnvironementPacket')
            return
        elif packet[0] == 'F':
            self.log.warning('parseFrienDDacket')
            return
        elif packet[0] == 'f':
            self.log.warning('parseFightPacket')
            return
        elif packet[0] == 'G':
            self.log.warning('parseGamePacket')
            return
        elif packet[0] == 'g':
            self.log.warning('parseGuildPacket')
            return
        elif packet[0] == 'h':
            self.log.warning('parseHousePacket')
            return
        elif packet[0] == 'i':
            self.log.warning('parseEnemyPacket')
            return
        elif packet[0] == 'J':
            self.log.warning('parseJobOption')
            return
        elif packet[0] == 'K':
            self.log.warning('parseHouseKodePacket')
            return
        elif packet[0] == 'O':
            self.log.warning('parseObjectPacket')
            return
        elif packet[0] == 'P':
            self.log.warning('parseGroupPacket')
            return
        elif packet[0] == 'R':
            self.log.warning('parseMountPacket')
            return
        elif packet[0] == 'Q':
            self.log.warning('parseQuestData')
            return
        elif packet[0] == 'S':
            self.log.warning('parseSpellPacket')
            return
        elif packet[0] == 'T':
            self.log.warning('parseFoireTroll')
            return
        elif packet[0] == 'W':
            self.log.warning('parseWaypointPacket')
            return

# --------------------------------------------------------------------
# PARSE ACCOUNT PACKET

    def parse_account_packet(self, gameClient, packet, exchangeTransferList):
        if packet[1] == 'A':
            self.log.warning('addCharacter')
            return
        elif packet[1] == 'B':
            self.log.warning('boost')
            return
        elif packet[1] == 'D':
            self.log.warning('deleteCharacter')
            return
        elif packet[1] == 'f':
            self.log.warning('getQueuePosition')
            self.get_queue_position(gameClient)
            return
        elif packet[1] == 'g':
            self.log.warning('getGifts')
            return
        elif packet[1] == 'G':
            self.log.warning('attributeGiftToCharacter')
            return
        elif packet[1] == 'i':
            self.log.warning('sendIdentity')
            self.send_identity(gameClient, packet)
            return
        elif packet[1] == 'L':
            self.log.warning('getCharacters')
            self.get_characters(gameClient)
            return
        elif packet[1] == 'M':
            self.log.warning('parseMigration')
            return
        elif packet[1] == 'S':
            self.log.warning('setCharacter')
            return
        elif packet[1] == 'T':
            self.log.warning('sendTicket')
            self.send_ticket(gameClient, packet, exchangeTransferList)
            return
        elif packet[1] == 'V':
            self.log.warning('requestRegionalVersion')
            self.socketManager.GAME_SEND_AV0(gameClient)
            return
        elif packet[1] == 'P':
            self.log.warning('SocketManager.REALM_SEND_REQUIRED_APK')
            self.socketManager.REALM_SEND_REQUIRED_APK(gameClient)
            return
    
    def get_queue_position(self, gameClient):
        # placeholder ¯\_(ツ)_/¯
        __queueID = 1
        __position = 1
        self.socketManager.MULTI_SEND_Af_PACKET(gameClient, __position, 1, 1, "1", __queueID)

    def send_identity(self, gameClient, packet):
        gameClient.get_account().set_key(packet[2:])

    def get_characters(self, gameClient):
        # both objects refer to each other    gameClient <-> account
        gameClient.get_account().set_game_client(gameClient)
        # TODO relog in the fight
        
        playerList = self.world.get_players_by_accid(gameClient.get_account().get_id())
        if len(playerList) == 0:
            pass
        self.socketManager.GAME_SEND_PLAYER_LIST(gameClient)

    def send_ticket(self, gameClient, packet, exchangeTransferList):
        accId = packet[2:]
        __accIsAvailable = False
        __delCount = 0
        for acc in exchangeTransferList:
            if str(acc.get_id()) == accId:
                gameClient.set_account(acc)
                __accIsAvailable = True
                del exchangeTransferList[__delCount]
            __delCount += 1
        if __accIsAvailable == True:
            self.socketManager.GAME_SEND_ATTRIBUTE_SUCCESS(gameClient)
        else:
            self.socketManager.GAME_SEND_ATTRIBUTE_FAILED(gameClient)
            gameClient.kick()        
        
        # TODO In my opinion, the queue is sent here (Main.gameServer.getWaitingCompte(id))
        # try:
            # try:
                # pass
                # this.compte = Main.gameServer.getWaitingCompte(id);
            # except Exception as e:
                # self.socketManager.GAME_SEND_ATTRIBUTE_FAILED(gameClient)
                # self.log.warning(e)
                # gameClient.kick()
            # String ip = this.session.getRemoteAddress().toString().substring(1).split("\\:")[0];
			# this.compte.setGameClient(this);
			# this.compte.setCurIP(ip);
            # Main.gameServer.delWaitingCompte(this.compte);
            # Database.getStatique().getPlayerData().loadByAccountId(this.compte.getGuid());
            # self.socketManager.GAME_SEND_ATTRIBUTE_SUCCESS(this);
        # except Exception as e:
        #     self.log.warning(e)
        #     gameClient.kick()

# --------------------------------------------------------------------
