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
import re

from common.socket_manager import SocketManager
from core.logging_handler import Logging
from game.game_client import GameClient


class GameHandler:

    def __init__(self, socket, addr, exchangeTransferList, world):
        self.log = Logging()
        self.world = world
        self.gameClient = GameClient(socket, addr)
        self.exchangeTransferList = exchangeTransferList
        self.socketManager = SocketManager(self.gameClient)

        self.socketManager.GAME_SEND_HELLOGAME_PACKET()
        self.loop()

    def loop(self):
        while True:
            data = self.gameClient.get_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n\x00', '[n][x00]')
            self.log.debug('[{}][ACC:{}][<-RECV] {}'.format(str(self.gameClient.get_addr()[0]),
                                                            str('X'),
                                                            str(packetLog)))
            if not data:
                self.log.debug('[{}][ACC:{}] PacketLoop no data'.format(str(self.gameClient.get_addr()[0]),
                                                                str('X')))
                self.gameClient.kick()
                break
            multiPacket = packet.split("\n\x00")
            if len(multiPacket) > 2:
                for p in multiPacket:
                    if not p == '':
                        self.parse(p)
            else:
                self.parse(packet.replace('\n\x00', ''))

# --------------------------------------------------------------------
# MAIN PARSE

    def parse(self, packet):
        if packet[0] == 'A':
            self.log.warning('parse_account_packet')
            self.parse_account_packet(packet)
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

    def parse_account_packet(self, packet):
        if packet[1] == 'A':
            self.log.warning('addCharacter')
            self.add_character(packet)
            return
        elif packet[1] == 'B':
            self.log.warning('boost')
            return
        elif packet[1] == 'D':
            self.log.warning('deleteCharacter')
            return
        elif packet[1] == 'f':
            self.log.warning('getQueuePosition')
            self.get_queue_position()
            return
        elif packet[1] == 'g':
            self.log.warning('getGifts')
            return
        elif packet[1] == 'G':
            self.log.warning('attributeGiftToCharacter')
            return
        elif packet[1] == 'i':
            self.log.warning('sendIdentity')
            self.send_identity(packet)
            return
        elif packet[1] == 'L':
            self.log.warning('getCharacters')
            self.get_characters()
            return
        elif packet[1] == 'M':
            self.log.warning('parseMigration')
            return
        elif packet[1] == 'S':
            self.log.warning('setCharacter')
            return
        elif packet[1] == 'T':
            self.log.warning('sendTicket')
            self.send_ticket(packet)
            return
        elif packet[1] == 'V':
            self.log.warning('requestRegionalVersion')
            self.socketManager.GAME_SEND_AV0()
            return
        elif packet[1] == 'P':
            self.log.warning('SocketManager.REALM_SEND_REQUIRED_APK')
            self.socketManager.REALM_SEND_REQUIRED_APK()
            return

    def add_character(self, packet):
        __packetList = packet[2:].split('|')
        __forbiddenWords = [r'[Aa][Dd][Mm][Ii][Nn]', r'[Mm][Oo][Dd][Oo]', r'[Gg][Mm]',
                            r'[Gg][Aa][Mm][Ee]-?[Mm][Aa][Ss][Tt][Ee][Rr]']
        __isValid = True
        for player in self.world.get_players():
            if player.get_name() == __packetList[0]:
                self.socketManager.GAME_SEND_NAME_ALREADY_EXIST()
                return
        for __f in __forbiddenWords:
            if re.search(__f, __packetList[0]):
                __isValid = False
        for __i in __packetList[0]:
            nick = re.match(r'[a-zA-Z]?\x2D?', __i)
            if nick.group(0) == '':
                __isValid = False
        if __isValid == False:
            self.socketManager.GAME_SEND_NAME_ALREADY_EXIST()
            return
        if self.gameClient.get_account().get_number_of_characters() >= 5:
            self.socketManager.GAME_SEND_CREATE_PERSO_FULL()
            return
        try:
            self.world.create_player(self.gameClient.get_account().get_id(),
                                    __packetList[0],int(__packetList[1]),int(__packetList[2]),
                                    int(__packetList[3]),int(__packetList[4]),int(__packetList[5]))

            __playerList = self.world.get_players_by_accid(self.gameClient.get_account().get_id())
            if len(__playerList) != 0:
                self.gameClient.get_account().set_characters(__playerList)

            self.socketManager.GAME_SEND_CREATE_OK()

            self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                    self.gameClient.get_account().get_number_of_characters(),
                                                    self.gameClient.get_account().get_characters())
            # self.socketManager.GAME_SEND_cMK_PACKET_TO_MAP()
        except Exception as e:
            self.socketManager.GAME_SEND_CREATE_FAILED()
            self.log.warning('[{}][ACC:{}] GameHandler.add_character Exception: {}'.format(str(self.gameClient.get_addr()[0]),
                                                                    str('X'),
                                                                    str(e)))

    def get_queue_position(self):
        # placeholder ¯\_(ツ)_/¯
        __queueID = 1
        __position = 1
        self.socketManager.MULTI_SEND_Af_PACKET(__position, 1, 1, "1", __queueID)

    def send_identity(self, packet):
        self.gameClient.get_account().set_key(packet[2:])

    def get_characters(self):
        # both objects refer to each other    gameClient <-> account
        self.gameClient.get_account().set_game_client(self.gameClient)
        # TODO relog in the fight

        __playerList = self.world.get_players_by_accid(self.gameClient.get_account().get_id())
        if len(__playerList) != 0:
            self.gameClient.get_account().set_characters(__playerList)
        self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                self.gameClient.get_account().get_number_of_characters(),
                                                self.gameClient.get_account().get_characters())

    def send_ticket(self, packet):
        __accId = packet[2:]
        __accIsAvailable = False
        __delCount = 0
        for acc in self.exchangeTransferList:
            if str(acc.get_id()) == __accId:
                self.gameClient.set_account(acc)
                __accIsAvailable = True
                del self.exchangeTransferList[__delCount]
            __delCount += 1
        if __accIsAvailable == True:
            self.socketManager.GAME_SEND_ATTRIBUTE_SUCCESS()
        else:
            self.socketManager.GAME_SEND_ATTRIBUTE_FAILED()
            self.gameClient.kick()

        # TODO In my opinion, the queue is sent here (Main.gameServer.getWaitingCompte(id))
        # try:
            # try:
                # pass
                # this.compte = Main.gameServer.getWaitingCompte(id);
            # except Exception as e:
                # self.socketManager.GAME_SEND_ATTRIBUTE_FAILED()
                # self.log.warning(e)
                # self.gameClient.kick()
            # String ip = this.session.getRemoteAddress().toString().substring(1).split("\\:")[0];
			# this.compte.setGameClient(this);
			# this.compte.setCurIP(ip);
            # Main.gameServer.delWaitingCompte(this.compte);
            # Database.getStatique().getPlayerData().loadByAccountId(this.compte.getGuid());
            # self.socketManager.GAME_SEND_ATTRIBUTE_SUCCESS(this);
        # except Exception as e:
        #     self.log.warning(e)
        #     self.gameClient.kick()

# --------------------------------------------------------------------
