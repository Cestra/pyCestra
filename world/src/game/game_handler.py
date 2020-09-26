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

        self.accId = None
        self.account = None

        self.socketManager.GAME_SEND_HELLOGAME_PACKET()
        self.loop()

    def loop(self):
        while True:
            data = self.gameClient.get_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n\x00', '[n][x00]')
            self.log.debug('[{}][ACC:{}][<-RECV] {}'.format(str(self.gameClient.get_addr()[0]),
                                                            str(self.acc_display_number()),
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

    def acc_display_number(self):
        if type(self.accId) != int:
            if self.account == None:
                self.accId = 'X'
            else:
                self.accId = self.gameClient.get_account().get_id()
        return self.accId

# --------------------------------------------------------------------
# MAIN PARSE

    def parse(self, packet):
        if packet[0] == 'A':
            # self.log.warning('parse_account_packet')
            self.parse_account_packet(packet)
            return
        elif packet[0] == 'B':
            self.log.warning('parseBasicsPacket')
            if packet[1] == 'D':
                self.socketManager.send('BT400000000000', 'BD (DEMO)')
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
            # self.log.warning('parseGamePacket')
            self.parse_game_packet(packet)
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
        else:
            self.log.warning('UNKNOWN MAIN PACKAGE ({})'.format(str(packet)))
            return

# --------------------------------------------------------------------
# PARSE ACCOUNT PACKET

    def parse_account_packet(self, packet):
        if packet[1] == 'A':
            # self.log.warning('addCharacter')
            self.add_character(packet)
            return
        elif packet[1] == 'B':
            self.log.warning('boost')
            return
        elif packet[1] == 'D':
            self.log.warning('deleteCharacter')
            self.delete_character(packet)
            return
        elif packet[1] == 'f':
            # self.log.warning('getQueuePosition')
            self.get_queue_position()
            return
        elif packet[1] == 'g':
            self.log.warning('getGifts')
            return
        elif packet[1] == 'G':
            self.log.warning('attributeGiftToCharacter')
            return
        elif packet[1] == 'i':
            # self.log.warning('sendIdentity')
            self.send_identity(packet)
            return
        elif packet[1] == 'L':
            # self.log.warning('getCharacters')
            self.get_characters()
            return
        elif packet[1] == 'M':
            self.log.warning('parseMigration')
            return
        elif packet[1] == 'S':
            # self.log.warning('setCharacter')
            self.set_character(packet)
            return
        elif packet[1] == 'T':
            # self.log.warning('sendTicket')
            self.send_ticket(packet)
            return
        elif packet[1] == 'V':
            # self.log.warning('requestRegionalVersion')
            self.socketManager.GAME_SEND_AV0()
            return
        elif packet[1] == 'P':
            # self.log.warning('SocketManager.REALM_SEND_REQUIRED_APK')
            self.socketManager.REALM_SEND_REQUIRED_APK()
            return
        else: 
            self.log.warning('UNKNOWN ACCOUNT PACKAGE ({})'.format(str(packet)))
            return

    def add_character(self, packet):
        __packetList = packet[2:].split('|')
        __forbiddenWords = [r'[Aa][Dd][Mm][Ii][Nn]', r'[Mm][Oo][Dd][Oo]', r'[Gg][Mm]',
                            r'[Gg][Aa][Mm][Ee]-?[Mm][Aa][Ss][Tt][Ee][Rr]']
        __isValid = True
        # check existing character names
        for player in self.world.get_players():
            if player.get_name() == __packetList[0]:
                self.socketManager.GAME_SEND_NAME_ALREADY_EXIST()
                return
        # check for forbidden words
        for __f in __forbiddenWords:
            if re.search(__f, __packetList[0]):
                __isValid = False
        # checking prohibited symbols
        for __i in __packetList[0]:
            nick = re.match(r'[a-zA-Z]?\x2D?', __i)
            if nick.group(0) == '':
                __isValid = False
        if __isValid == False:
            self.socketManager.GAME_SEND_NAME_ALREADY_EXIST()
            return
        # check available character slots
        if self.gameClient.get_account().get_number_of_characters() >= 5:
            self.socketManager.GAME_SEND_CREATE_PERSO_FULL()
            return
        try:
            self.world.create_player(self.gameClient.get_account().get_id(),
                                    __packetList[0],int(__packetList[1]),int(__packetList[2]),
                                    int(__packetList[3]),int(__packetList[4]),int(__packetList[5]))
            # # save changes in the account class
            __playerList = self.world.get_players_by_accid(self.gameClient.get_account().get_id())
            if len(__playerList) != 0:
                self.gameClient.get_account().set_characters(__playerList)
            self.socketManager.GAME_SEND_CREATE_OK()
            # # broadcast of the current player list
            self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                    self.gameClient.get_account().get_number_of_characters(),
                                                    self.gameClient.get_account().get_characters())
            self.socketManager.GAME_SEND_cMK_PACKET_TO_MAP()
        except Exception as e:
            self.socketManager.GAME_SEND_CREATE_FAILED()
            self.log.warning('[{}][ACC:{}] GameHandler.add_character Exception: {}'.format(str(self.gameClient.get_addr()[0]),
                                                                                            str('X'),
                                                                                            str(e)))

    def delete_character(self, packet):
        try:
            __packetList = packet[2:].split('|')
            # determine the position of the character, save the character
            displayPosition = int(__packetList[0])
            deletion_target = self.gameClient.get_account().get_characters().get(displayPosition)
            # check if the player is above level 19 and if the answer is correct
            if (deletion_target.get_level() >= 20 and __packetList[1] == self.gameClient.get_account().get_reponse()) or deletion_target.get_level() < 20:
                self.world.delete_player(deletion_target.get_id())
                # save changes in the account class
                __playerList = self.world.get_players_by_accid(self.gameClient.get_account().get_id())
                if len(__playerList) != 0:
                    self.gameClient.get_account().set_characters(__playerList)
                # broadcast of the current player list
                self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                        self.gameClient.get_account().get_number_of_characters(),
                                                        self.gameClient.get_account().get_characters())
            else:
                self.socketManager.GAME_SEND_DELETE_PERSO_FAILED()
        except Exception as e:
            self.socketManager.GAME_SEND_DELETE_PERSO_FAILED()
            self.log.warning('[{}][ACC:{}] GameHandler.delete_character Exception: {}'.format(str(self.gameClient.get_addr()[0]),
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
        self.gameClient.get_account().set_characters(__playerList)
        self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                self.gameClient.get_account().get_number_of_characters(),
                                                self.gameClient.get_account().get_characters())
    
    def set_character(self, packet):
        try:
            __listPosition = int(packet[2:])
            self.gameClient.get_account().set_player(__listPosition)
        except Exception as e:
            self.socketManager.GAME_SEND_PERSO_SELECTION_FAILED()
            self.log.warning('[{}][ACC:{}] GameHandler.set_character Exception: {}'.format(str(self.gameClient.get_addr()[0]),
                                                                                            str('X'),
                                                                                            str(e)))
            self.gameClient.kick()

        self.log.warning('set_character !!! full of placeholders !!!')
        self.socketManager.GAME_SEND_Rx_PACKET()
		# SocketManager.GAME_SEND_ASK(out, this);
                        # ID NAME LEVEL MORPH/CLASS SEXY GFXID COLOR(1-3) ItemToASK
        packet_ASK = 'ASK|1|Cestra|1|8|0|80|-1|-1|-1|'
        self.socketManager.send(packet_ASK, 'packet_ASK (DEMO)')
        self.socketManager.send("ILS2000", "ILS2000 (DEMO)")
        self.socketManager.send("ZS0", "GAME_SEND_ALIGNEMENT (DEMO)")
        self.socketManager.send("cC+i", "GAME_SEND_ADD_CANAL (DEMO)")
        self.socketManager.send("eL", "GAME_SEND_EMOTE_LIST (DEMO)")
        self.socketManager.send("AR6bk", "GAME_SEND_RESTRICTIONS (DEMO)")
        self.socketManager.send("Ow0|1000", "GAME_SEND_Ow_PACKET (DEMO)")

        text1 = 'cs<font color=\'#B9121B\'>'
        test2 = '</font>'
        mess = 'Powered by <b>Cestra</b>'
        text1 += mess + test2
        self.socketManager.send(text1, 'GAME_SEND_MESSAGE (DEMO)')

    def send_ticket(self, packet):
        __accId = packet[2:]
        __accIsAvailable = False
        __delCount = 0
        for acc in self.exchangeTransferList:
            if str(acc.get_id()) == __accId:
                self.gameClient.set_account(acc)
                self.account = acc
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
# PARSE GAME PACKET  parseGamePacket

    def parse_game_packet(self, packet):
        if packet[1] == 'A':
            self.log.warning('sendActions')
            return
        elif packet[1] == 'C':
            self.log.warning('sendGameCreate')
            self.send_game_create()
            return
        elif packet[1] == 'D':
            self.log.warning('deleteCharacter')
            return
        elif packet[1] == 'd':
            self.log.warning('showMonsterTarget')
            return
        elif packet[1] == 'f':
            self.log.warning('setFlag')
            return
        elif packet[1] == 'F':
            self.log.warning('set_Ghosts')
            return
        elif packet[1] == 'I':
            self.log.warning('getExtraInformations')
            self.get_extra_informations()
            return
        elif packet[1] == 'K':
            self.log.warning('actionAck')
            return
        elif packet[1] == 'P':
            self.log.warning('toggleWings')
            return
        elif packet[1] == 'p':
            self.log.warning('setPlayerPosition')
            return
        elif packet[1] == 'Q':
            self.log.warning('leaveFight')
            return
        elif packet[1] == 'R':
            self.log.warning('readyFight')
            return
        elif packet[1] == 't':
            self.log.warning('get_fight().playerPass')
            return
        else:
            self.log.warning('UNKNOWN GAME PACKAGE ({})'.format(str(packet)))
            return

    def send_game_create(self):

        self.socketManager.send('GCK|1|Cestra', 'GAME_SEND_GAME_CREATE (DEMO)')

        # GAME_SEND_STATS_PACKET
        #     GAME_SEND_Ow_PACKET
        # As	xp | _kamas | _capital | _spellPts | _align ~ _align , _aLvl , getGrade , _honor , _deshonor , 0 | curPdv , pdvMax | getEnergy , 10000 | getInitiative | 0 | 0,0,0,0,0 | 0,0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0| 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 |
        packet_As = 'As1,1,1|10000|5|6|0~3,0,0,0,0,0|10,100|10000,10000|100|0|0,0,0,0,0|0,0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|'
        self.socketManager.send(packet_As, 'GAME_SEND_GAME_CREATE (DEMO)')

        mapID = '7411'
        data = '0711291819'
        key = '556a5867706b7f7f694d754537565e7d437357343b49337d7a455d3c722a4974415445242e654c277c542f246f7764593831672c3f65227725324274565c692532422f2e3e2f726934556c512e387f4e75447b3e475b2972642c64685a33374b2a555d4c5f4f435c612d64566c2e2e38695248205b4c5c5a4c6242512947213536747d5f522d582d366b26647d2d73576a6b487b5f574a225a3440543a405a517551522d622a403d4a486477675646725f3367677c7d2934657f32663e46634064233d48677f3b524b2c352f402922744167333f7c5d7076674f43'
        packet_GDM = 'GDM|' + mapID + '|'  + data + '|'  + key
        self.socketManager.send(packet_GDM, 'packet_GDM (DEMO)')

        self.socketManager.send('fC0', 'packet_GDM (DEMO)')

    def get_extra_informations(self):
        # EndFightAction are checked here
        self.log.warning('EndFightAction are checked here')
        self.get_extra_informations_two()
        pass

    def get_extra_informations_two(self):
        try:
            # if (perso.get_fight() != null)
                # SocketManager.GAME_SEND_MAP_GMS_PACKETS(this.perso.get_fight().getMap(), this.perso);
                # SocketManager.GAME_SEND_GDK_PACKET(this);
                # return
            # House.load
            # SocketManager.GAME_SEND_MAP_GMS_PACKETS
            # SocketManager.GAME_SEND_MAP_MOBS_GMS_PACKETS
            # SocketManager.GAME_SEND_MAP_NPCS_GMS_PACKETS
            # SocketManager.GAME_SEND_MAP_PERCO_GMS_PACKETS
            # SocketManager.GAME_SEND_MAP_OBJECTS_GDS_PACKETS
            # SocketManager.GAME_SEND_GDK_PACKET
            # SocketManager.GAME_SEND_MAP_FIGHT_COUNT
            # SocketManager.SEND_GM_PRISME_TO_MAP
            # SocketManager.GAME_SEND_MERCHANT_LIST
            # Fight.FightStateAddFlag
            # SocketManager.GAME_SEND_Rp_PACKET
            # SocketManager.GAME_SEND_GDO_OBJECT_TO_MAP
            # SocketManager.GAME_SEND_GM_MOUNT
            # sendFloorItems
            # verifDoor
            # World.showPrismes
            # for (final Player player : this.perso.getCurMap().getPersos())
            # 	player.send(String.valueOf(packet) + data)
			# 	this.perso.send(String.valueOf(packet) + data)
            pass
        except Exception as e:
            self.log.warning('[{}][ACC:{}] GameHandler.get_extra_informations_two Exception: {}'.format(str(self.gameClient.get_addr()[0]),
                                                                                                        str('X'),
                                                                                                        str(e)))

# --------------------------------------------------------------------
