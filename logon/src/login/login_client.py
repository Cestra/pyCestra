import socket
import threading
from enum import Enum

from _thread import start_new_thread
from core.logging_handler import Logging


class LoginClient:

    def __init__(self, c, key, addr):
        self.log = Logging()
        self.log.debug('LoginClient erstellt - '+ str(addr[0])+ ':'+ str(addr[1])+ ' - '+key)

        LoginClient.set_key(key)

        message = 'HC'+key
        c.send(message.encode('utf-8'))

        while True:
            c.send(message.encode('utf-8'))
            data = c.recv(1024)
            if not data:
                print('0 DATA')
                self.log.info('Disconnected '+ str(addr[0])+ ':'+ str(addr[1]))
                break
            # msg = data.decode()
            # print(self.addr[1], ': "', msg, '"')
        c.close()

    def send(self):
        pass

    def parser(self):
        pass

    def kick(self):
        pass

    def get_id(self):
        pass

    def set_id(self):
        pass

    def get_io_session(self):
        pass

    def get_key(self, key):
        return key

    def set_key(self):
        pass

    def get_status(self):
        pass

    def set_status(self):
        pass

    def get_account(self):
        pass

    def set_account(self):
        pass

    def status(self, Enum):
        '''
        WAIT_VERSION = "WAIT_VERSION", 0
        WAIT_PASSWORD = "WAIT_PASSWORD", 1
        WAIT_ACCOUNT = "WAIT_ACCOUNT", 2
        WAIT_NICKNAME = "WAIT_NICKNAME", 3
        SERVER = "SERVER", 4
        '''
