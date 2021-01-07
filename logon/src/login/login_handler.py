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

import random
import threading
from enum import Enum

from core.logging_handler import Logging
from login.hello_connection import HelloConnection
from login.login_client import LoginClient
from login.packet.packet_handler import PacketHandler


class LoginHandler:

    def __init__(self, soecket ,addr, gameClientDic, accountDataDic, hostList, ipbans):
        self.log = Logging()
        self.gameClientDic = gameClientDic
        self.accountDataDic = accountDataDic
        self.hostList = hostList

        self.client = LoginClient(self.gameClientDic, self.accountDataDic)
        self.client.set_key(self.generate_key())
        self.client.set_address(addr)
        self.client.set_status(Status(0))
        self.client.set_io_session(soecket)

        self.log.debug('[' + str(addr[0]) + ':' + str(addr[1]) + '][' +
                        str(self.client.get_status().name) + '] Client created - '+ self.client.get_key())

        # the object is save in the global dictionary
        dict_str = addr[0] + ':' + str(addr[1])
        self.gameClientDic[dict_str] = self.client

        HelloConnection(self.client, ipbans)
        self.recv_loop()

    def recv_loop(self):
        packetHandler = PacketHandler()
        while True:
            data = self.client.get_io_session().recv(2048)
            packet = data.decode()
            packetPrint = packet.replace('\n', '[n]')
            self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                            str(self.client.get_address()[1]) + ']' +
                            '[' + str(self.client.get_status().name) + '][<-RECV] ' +
                            packetPrint)
            if not data:
                self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                            str(self.client.get_address()[1]) + ']' +
                            '[' + str(self.client.get_status().name) + '] PacketLoop no data')
                self.client.kick()
                break
            packetHandler.parser(self.client, packet, self.gameClientDic,
                                self.accountDataDic, self.hostList)

    def send_to_all(self):
        pass

    def generate_key(self):
        key = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        while len(key) < 32:
            char = random.choice(alphabet)
            key += char
        # key = key[:-1]
        return key

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
