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
from login.login_handler import LoginHandler


class LoginServer:

    def __init__(self, ip, port, gameClientDic, accountDataDic, hostList, ipBans):
        self.log = Logging()
        self.logoniIP = ip
        self.logonPort = port
        self.gameClientDic = gameClientDic
        self.accountDataDic = accountDataDic
        self.hostList = hostList
        self.ipBans = ipBans

        self.start()

    def start(self):
        threadName = 'Login-Server - ' + str(self.logonPort)
        try:
            t = threading.Thread(target=self.server,
                                name=threadName,
                                args=(self.logoniIP, self.logonPort,
                                    self.gameClientDic, self.accountDataDic,
                                    self.hostList, self.ipBans))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Login Server could not be created: ' + str(e))

    def server(self, logoniIP, logonPort, gameClientDic, accountDataDic, hostList, ipBans):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.logoniIP, self.logonPort))
        except socket.error:
            print('Login Socket - Binding faild')
        s.listen()
        self.log.info('Logon Socket is listening on Port: ' + str(self.logonPort))
        while True:
            c, self.addr = s.accept()
            self.log.info('[{}:{}] Client Connected '.format(str(self.addr[0]),str(self.addr[1])))
            self.session_created(c, self.addr)
        s.close()

    def session_created(self, soecket, addr):
        threadName = 'Client-Session '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=LoginHandler,
                                name=threadName,
                                args=(soecket, addr, self.gameClientDic,
                                    self.accountDataDic, self.hostList, self.ipBans))
            t.start()
        except threading.ThreadError as e:
            self.log.debug('Created Session '+ str(addr[0])+':'+ str(addr[1]) + ': ' + str(e))
