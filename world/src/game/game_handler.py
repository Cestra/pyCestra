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
# PARSE ACCOUNT PACKET

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
                                                                                            str(self.acc_display_number()),
                                                                                            str(e)))

    def boost(self, packet):
        self.log.warning('boost')

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
                                                                                            str(self.acc_display_number()),
                                                                                            str(e)))

    def get_queue_position(self, packet):
        # placeholder ¯\_(ツ)_/¯
        __queueID = 1
        __position = 1
        self.socketManager.MULTI_SEND_Af_PACKET(__position, 1, 1, "1", __queueID)

    def get_gifts(self, packet):
        self.log.warning('getGifts')

    def attribute_gift_to_character(self, packet):
        self.log.warning('attributeGiftToCharacter')

    def send_identity(self, packet):
        self.gameClient.get_account().set_key(packet[2:])

    def get_characters(self, packet):
        # both objects refer to each other    gameClient <-> account
        self.gameClient.get_account().set_game_client(self.gameClient)
        # TODO relog in the fight

        __playerList = self.world.get_players_by_accid(self.gameClient.get_account().get_id())
        self.gameClient.get_account().set_characters(__playerList)
        self.socketManager.GAME_SEND_PLAYER_LIST(self.gameClient.get_account().get_subscribe(),
                                                self.gameClient.get_account().get_number_of_characters(),
                                                self.gameClient.get_account().get_characters())

    def parse_migration(self, packet):
        self.log.warning('parseMigration')

    def set_character(self, packet):
        try:
            __listPosition = int(packet[2:])
            self.gameClient.get_account().set_player(__listPosition)
            # both objects refer to each other    account <-> player
            self.gameClient.get_account().get_player().set_account(self.gameClient.get_account(), self.socketManager)
            self.gameClient.get_account().get_player().join_game()
        except Exception as e:
            self.socketManager.GAME_SEND_PERSO_SELECTION_FAILED()
            self.log.warning('[{}][ACC:{}] GameHandler.set_character Exception: {}'.format(str(self.gameClient.get_addr()[0]),
                                                                                            str(self.acc_display_number()),
                                                                                            str(e)))
            self.gameClient.kick()

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

    def request_regional_version(self, packet):
        self.socketManager.GAME_SEND_AV0()
    
    def realm_send_required_apk(self, packet):
        self.socketManager.REALM_SEND_REQUIRED_APK()

# --------------------------------------------------------------------
# PARSE GAME PACKET  parseBasicsPacket

    def get_date(self, packet):
        self.socketManager.GAME_SEND_SERVER_HOUR()

# --------------------------------------------------------------------
# PARSE GAME PACKET  parseGamePacket

    def send_actions(self, packet):
        self.log.warning('sendActions')

    def send_game_create(self, packet):
            self.gameClient.get_account().get_player().send_game_create()

    def delete_character_GD(self, packet):
        self.log.warning('deleteCharacter')

    def show_monster_target(self, packet):
        self.log.warning('showMonsterTarget')

    def set_flag(self, packet):
        self.log.warning('setFlag')

    def set_ghosts(self, packet):
        self.log.warning('setFlag')

    def get_extra_informations(self, packet):
        # EndFightAction are checked here
        self.log.warning('EndFightAction are checked here')
        self.get_extra_informations_two(packet)
        pass

    def get_extra_informations_two(self, packet):
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
            self.socketManager.send('GDF|', 'GAME_SEND_MAP_OBJECTS_GDS_PACKETS (DEMO)')
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
                                                                                                        str(self.acc_display_number()),
                                                                                                        str(e)))

    def action_ack(self, packet):
        self.log.warning('actionAck')

    def toggle_wings(self, packet):
        self.log.warning('toggleWings')

    def set_player_position(self, packet):
        self.log.warning('setPlayerPosition')

    def leave_fight(self, packet):
        self.log.warning('leaveFight')

    def ready_fight(self, packet):
        self.log.warning('readyFight')

    def get_fight_player_pass(self, packet):
        self.log.warning('get_fight().playerPass')

# --------------------------------------------------------------------

    def parse(self, recPacked):
        packetParse = {
                    'AA' : self.add_character,
                    'AB' : self.boost,
                    'AD' : self.delete_character,
                    'Af' : self.get_queue_position,
                    'Ag' : self.get_gifts,
                    'AG' : self.attribute_gift_to_character,
                    'Ai' : self.send_identity,
                    'AL' : self.get_characters,
                    'AM' : self.parse_migration,
                    'AS' : self.set_character,
                    'AT' : self.send_ticket,
                    'AV' : self.request_regional_version,
                    'AP' : self.realm_send_required_apk,
                    'BD' : self.get_date,
                    'GA' : self.send_actions,
                    'GC' : self.send_game_create,
                    'GD' : self.delete_character_GD,
                    'Gd' : self.show_monster_target,
                    'Gf' : self.set_flag,
                    'GF' : self.set_ghosts,
                    'GI' : self.get_extra_informations,
                    'GK' : self.action_ack,
                    'GP' : self.toggle_wings,
                    'Gp' : self.set_player_position,
                    'GQ' : self.leave_fight,
                    'GR' : self.ready_fight,
                    'Gt' : self.get_fight_player_pass,
        }

        try:
            packetParse[recPacked[:2]](recPacked)
        except KeyError:
            self.log.warning('UNKNOWN PACKAGE {}({})'.format(recPacked[:2],recPacked))
