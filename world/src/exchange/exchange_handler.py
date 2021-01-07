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

from core.logging_handler import Logging
from exchange.exchange_packet_handler import ExchangePacketHandler


class ExchangeHandler:

    def __init__(self):
        self.log = Logging()

    def loop(self, exSocket, exchangeTransferList):
        self.log.debug('Exchange-Receiver is started')
        while True:
            data = exSocket.recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[logon ip][<-EX-RECV] '
                            + packetLog)
            if not data:
                self.log.debug('[logon ip] PacketLoop no data')
                # kick
                break
            ExchangePacketHandler().parser(packet, exSocket, exchangeTransferList)
