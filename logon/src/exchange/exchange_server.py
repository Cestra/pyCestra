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
import threading

from core.logging_handler import Logging
from exchange.exchange_handler import HelloExchangeClient


class ExchangeServer():

    def __init__(self):
        self.log = Logging()

    def start(self, ip, port, hostList):
        threadName = 'Exchange-Server - ' + str(port)
        try:
            t = threading.Thread(target=ExchangeServer.server,
                                name=threadName,
                                args=(self, ip, port, hostList))
            t.start()
        except:
            self.log.warning('Exchange Server could not be created')

    def server(self, ex_ip, ex_port, hostList):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ex_ip, ex_port))
        except socket.error:
            self.log.warning('Exchange Socket - Binding faild')
        s.listen()
        self.log.info('Exchange Socket is listening on Port: ' + str(ex_port))
        while True:
            c, self.addr = s.accept()
            self.log.info('Exchange Client connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            ExchangeServer().session_created(c, self.addr, hostList)
        s.close()

    def session_created(self, soecket, addr, hostList):
        threadName = 'Exchange-Client '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=HelloExchangeClient,
                                name=threadName,
                                args=(soecket, addr, hostList))
            t.start()
        except:
            self.log.warning('Exchange Client could not be created '+ str(addr[0])+':'+ str(addr[1]))
