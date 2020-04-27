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
from client.account import Account

class ExchangePacketHandler:

    def __init__(self):
        self.log = Logging()

    def parser(self, packet, exClient, exchangeTransferList):
        if packet[0] == 'F':
            if packet[1] == '?': # F?
                # i = 50000 - Main.gameServer.getPlayerNumber()
                # exchangeClient.send("F" + i)
                return
            return
        elif packet[0] == 'S':
            if packet[1] == 'H':
                if packet[2] == 'K': # SHK
                    self.log.debug('The Logon-Server validates the connection successfully.')
                    return
                return
            elif packet[1] == 'K':
                if packet[2] == '?': # SK?
                    i = 50000 - 0 # Main.gameServer.getPlayerNumber()
					# TODO Main.exchangeClient.send("SK" + Main.serverId + ";" + Main.key + ";" + i)
                    ExchangePacketHandler().send(exClient,'SK1;demo;' + str(i))
                    return
                elif packet[2] == 'K': # SKK
                    self.log.debug('The Logon-Server has accepted the connection')  
					# TODO Main.exchangeClient.send("SH" + Main.Ip + ";" + Main.gamePort)
                    ExchangePacketHandler().send(exClient,'SH' + '127.0.0.1' + ';' + '5555')
                    return
                elif packet[2] == 'R': # SKR
					# self.log.debug('The login server refused the connection')
					# Main.stop()
                    return
                return
            return
        elif packet[0] == 'W':
            # if (packet.split("W").length > 2)
                # magic !
            if packet[1] == 'A': # WA
                packet = packet.split("#")
                account = Account(int(packet[1]),
                                packet[2],
                                packet[3],
                                packet[4],
                                int(packet[5]),
                                packet[6],
                                packet[7])
                exchangeTransferList.append(account)
                return
            elif packet[1] == 'K': # WK
                return
            return
        elif packet[0] == 'M':
            if packet[1] == 'G': # MG
                return
            if packet[1] == 'F': # MF
                return
            if packet[1] == 'D': # MD
                return
            return

    def send(self, exClient, o):
        msg = bytes(o, 'utf-8')
        self.log.debug('[logon ip]' +
                '[EX-SEND->] ' + o)
        exClient.send(msg)
