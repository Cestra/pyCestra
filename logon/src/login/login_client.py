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

import sys
from enum import Enum

from core.logging_handler import Logging


class LoginClient:

    def __init__(self, game_client_dic, accountDataDic):
        self.game_client_dic = game_client_dic
        self.accountDataDic = accountDataDic
        self.log = Logging()

    def write(self, o):
        msg = bytes(o+'\x00', 'utf-8')
        self.log.debug('[' + str(self.address[0]) + ':' +
                    str(self.address[1]) + '][' +
                    str(self.status.name) + '][SEND->] ' + o)
        self.IoSession.send(msg)

    def kick(self):
        # -----------------------------------------
        # update 'logged' to 0
        try:
            for i in self.accountDataDic:
                if i['id'] == self.account.get_id():
                    i['logged'] = 0
        except AttributeError:
            self.log.debug('[{}:{}][{}] The Login-Client was kicked so early that no account was set up yet'.format(str(self.address[0]),
                                                                                                            str(self.address[1]),
                                                                                                            str(self.status.name)))
        # -----------------------------------------
        # delete entries in 'game_client_dic'
        dict_str = self.address[0] + ':' + str(self.address[1])
        self.IoSession.close()
        try:
            self.game_client_dic.pop(dict_str)
        except KeyError:
            self.log.warning('[' + str(self.address[0]) + ':' +
                            str(self.address[1]) + '][' +
                            str(self.status.name) +
                            '] The request in "game_client_dic" has been incorrectly removed')
        # -----------------------------------------
        self.log.info('[' + str(self.address[0]) + ':' +
                    str(self.address[1]) + '][' +        
                    str(self.status.name) + '] Client kick')
        sys.exit(0)

    def get_address(self):
        return self.address

    def set_address(self, a):
        self.address = a

    def get_id(self):
        return self.id

    def set_id(self, Client_id):
        self.id = Client_id

    def get_io_session(self):
        return self.IoSession

    def set_io_session(self, s):
        self.IoSession = s

    def get_key(self):
        return self.key

    def set_key(self, k):
        self.key = k

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account = account

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
