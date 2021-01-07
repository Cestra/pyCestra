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

import socket
import sys
import threading

from core.logging_handler import Logging
from exchange.exchange_handler import ExchangeHandler


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def initialize(self, exchange_ip, exchange_port, exchangeTransferList):
        try:
            exSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            exSocket.connect((exchange_ip, exchange_port))
            self.log.info('Exchange-Client connected to logon server ' +
                            str(exchange_ip) + ':' + str(exchange_port))
            self.ioConnector = exSocket
        except:
            exSocket.close()
            self.log.warning('It could not be connected to the login server')
            sys.exit(0)
        try:
            exchangeHandler = ExchangeHandler()
            threadName = 'Exchange-Receiver - Port: '+str(exchange_port)
            t = threading.Thread(target=exchangeHandler.loop,
                                name=threadName,
                                args=(self.ioConnector, exchangeTransferList,))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Exchange-Receiver could not be created ' + str(e))

        return self.ioConnector
