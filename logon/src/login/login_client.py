import sys
from enum import Enum

from core.logging_handler import Logging
from dataSource.account_data import AccountData


class LoginClient:

    def __init__(self, game_client_dic):
        self.game_client_dic = game_client_dic
        self.log = Logging()

    def write(self, o):
        msg = bytes(o+'\x00', 'utf-8')
        self.log.debug('[' + str(self.address[0]) + ':' +
                    str(self.address[1]) + '][' +
                    str(self.status.name) + '][SEND->] ' + o)
        self.IoSession.send(msg)

    def parser(self):
        pass

    def kick(self):
        # -----------------------------------------
        # update 'logged' to 0
        try:
            AccountData().single_update(self.account.get_id(),'logged',0)
        except AttributeError:
            self.log.debug('[' + str(self.address[0]) + ':' +
                    str(self.address[1]) + '][' +        
                    str(self.status.name) + '] self.account not set')
            pass
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

    def set_account(self, accountTupel):
        self.account = accountTupel

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
