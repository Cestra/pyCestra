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
import sys

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

        self.defaultrRun = True

        self.start()

    def start(self):
        threadName = 'Login-Server - ' + str(self.logonPort)
        try:
            self.t = threading.Thread(target=self.server,
                                    name=threadName,
                                    args=(self.defaultrRun,))
            self.t.start()
        except threading.ThreadError as e:
            self.log.warning('Login Server could not be created: ' + str(e))

    def server(self, arg):
        do_run = arg
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((self.logoniIP, self.logonPort))
            self.s.listen()
            self.log.info('Logon Socket is listening on Port: ' + str(self.logonPort))
        except socket.error:
            self.log.warning('Login Socket - Binding faild')
            sys.exit()
        while do_run:
            self.log.warning("while loop")
            try:
                c, self.addr = self.s.accept()
                self.log.info('[{}:{}] Client Connected '.format(str(self.addr[0]),str(self.addr[1])))
                self.session_created(c, self.addr)
            except socket.timeout:
                self.log.info("[{}:{}] Login Socket - TIMEOUT".format(str(self.addr[0]),str(self.addr[1])))
                continue
            except OSError:
                self.log.info("[{}:{}] Login Socket was killed".format(str(self.addr[0]),str(self.addr[1])))
        self.s.close()
        self.log.warning("ende des while !!!!!!!!!!!!!!!!")
    
    def stop(self):
        self.log.warning("stop - start")
        self.t.do_run = False
        self.log.warning("1")
        sys.exit()

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
