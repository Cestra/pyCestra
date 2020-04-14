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

from core.logging_handler import Logging

class SocketManager:

    def __init__(self):
        self.log = Logging()
    
    def send(self, gameClient, packet, name):
        msg = bytes(packet + '\x00', 'utf-8')
        gameClient.get_session().send(msg)
        self.log.debug('[{}][ACC:{}][SEND->] {} ({})'.format(str(gameClient.get_addr()[0]),
                                                        str('X'),
                                                        str(packet),
                                                        name))

    def GAME_SEND_HELLOGAME_PACKET(self, gameClient):
        __name = 'GAME_SEND_HELLOGAME_PACKET'
        __packet = 'HG'
        SocketManager().send(gameClient, __packet, __name)

    def GAME_SEND_ATTRIBUTE_FAILED(self, gameClient):
        __name = 'GAME_SEND_ATTRIBUTE_FAILED'
        __packet = 'ATE'
        SocketManager().send(gameClient, __packet, __name)

    def GAME_SEND_ATTRIBUTE_SUCCESS(self, gameClient):
        __name = 'GAME_SEND_ATTRIBUTE_SUCCESS'
        __packet = 'ATK0'
        SocketManager().send(gameClient, __packet, __name)
