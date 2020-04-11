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

import socket
import threading

from core.logging_handler import Logging
from login.login_handler import LoginHandler


class LoginServer:

    def __init__(self):
        self.log = Logging()

    def start(self, ip, port, game_client_dic, accountDataDic, hostList, ipbans):
        threadName = 'Login-Server - ' + str(port)
        try:
            t = threading.Thread(target=LoginServer.server,
                                name=threadName,
                                args=(self, ip, port, game_client_dic, accountDataDic, hostList, ipbans))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Login Server could not be created: ' + str(e))

    def server(self, logon_ip, login_port, game_client_dic, accountDataDic, hostList, ipbans):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((logon_ip, login_port))
        except socket.error:
            print('Login Socket - Binding faild')
        s.listen()
        self.log.info('Logon Socket is listening on Port: ' + str(login_port))
        while True:
            c, self.addr = s.accept()
            self.log.info('[{}:{}] Client Connected '.format(str(self.addr[0]),str(self.addr[1])))
            LoginHandler().session_created(c, self.addr, game_client_dic, accountDataDic, hostList, ipbans)
        s.close()
