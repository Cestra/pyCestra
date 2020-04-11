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


class GameHandler:

    def __init__(self):
        self.log = Logging()

    def loop(self, gameClient):
        while True:
            data = gameClient.get_io_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[TODO client ip][<-GM-RECV] '
                            + packetLog)
            if not data:
                self.log.debug('[TODO client ip] PacketLoop no data')
                gameClient.kick()
                break
            GameHandler.parse(packet)

    def session_created(self, soecket, addr):
        threadName = 'Game-Client-Session '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=GameClient,
                                name=threadName,
                                args=(soecket, addr,))
            t.start()
        except:
            self.log.warning('Game Client could not be created '+ str(addr[0])+':'+ str(addr[1]))

    def parse(self, packet):
        if packet[0] == 'A':
            print('parse_account_packet')
            return
        elif packet[0] == 'B':
            print('parseBasicsPacket')
            return
        elif packet[0] == 'C':
            print('parseConquestPacket')
            return
        elif packet[0] == 'c':
            print('parseChanelPacket')
            return
        elif packet[0] == 'D':
            print('parseDialogPacket')
            return
        elif packet[0] == 'd':
            print('parseDocumentPacket')
            return
        elif packet[0] == 'E':
            print('parseExchangePacket')
            return
        elif packet[0] == 'e':
            print('parseEnvironementPacket')
            return
        elif packet[0] == 'F':
            print('parseFrienDDacket')
            return
        elif packet[0] == 'f':
            print('parseFightPacket')
            return
        elif packet[0] == 'G':
            print('parseGamePacket')
            return
        elif packet[0] == 'g':
            print('parseGuildPacket')
            return
        elif packet[0] == 'h':
            print('parseHousePacket')
            return
        elif packet[0] == 'i':
            print('parseEnemyPacket')
            return
        elif packet[0] == 'J':
            print('parseJobOption')
            return
        elif packet[0] == 'K':
            print('parseHouseKodePacket')
            return
        elif packet[0] == 'O':
            print('parseObjectPacket')
            return
        elif packet[0] == 'P':
            print('parseGroupPacket')
            return
        elif packet[0] == 'R':
            print('parseMountPacket')
            return
        elif packet[0] == 'Q':
            print('parseQuestData')
            return
        elif packet[0] == 'S':
            print('parseSpellPacket')
            return
        elif packet[0] == 'T':
            print('parseFoireTroll')
            return
        elif packet[0] == 'W':
            print('parseWaypointPacket')
            return

    def parse_account_packet(self, packet):
        if packet[1] == 'A':
            print('addCharacter')
            return
        elif packet[1] == 'B':
            print('boost')
            return
        elif packet[1] == 'D':
            print('deleteCharacter')
            return
        elif packet[1] == 'f':
            print('getQueuePosition')
            return
        elif packet[1] == 'g':
            print('getGifts')
            return
        elif packet[1] == 'G':
            print('attributeGiftToCharacter')
            return
        elif packet[1] == 'i':
            print('sendIdentity')
            return
        elif packet[1] == 'L':
            print('getCharacters')
            return
        elif packet[1] == 'M':
            print('parseMigration')
            return
        elif packet[1] == 'S':
            print('setCharacter')
            return
        elif packet[1] == 'T':
            print('sendTicket')
            return
        elif packet[1] == 'V':
            print('requestRegionalVersion')
            return
        elif packet[1] == 'P':
            print('SocketManager.REALM_SEND_REQUIRED_APK')
            return
