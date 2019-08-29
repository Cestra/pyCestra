import socket
import threading
from enum import Enum

from core.logging_handler import Logging


class LoginClient:

    def __init__(self, c, key, addr):
        self.log = Logging()
        self.log.debug('LoginClient erstellt - '+ str(addr[0])+ ':'+ str(addr[1])+ ' - '+key)

        self.setId = addr[0]
        self.setIoSession = c
        self.setKey = key

        message = 'HC'+key
        while True:
            c.send(message.encode('utf-8'))
            data = c.recv(1024)
            if not data:
                print('0 DATA')
                self.log.info('Disconnected '+ str(addr[0])+ ':'+ str(addr[1]))
                break
            msg = data.decode()
            self.log.debug(str(addr[1])+ ': "'+ msg+ '"')
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
        return self.setId

    def get_io_session(self):
        return self.setIoSession

    def set_io_session(self):
        pass

    def get_key(self):
        return self.setKey

    def set_key(self):
        pass

    def get_status(self):
        pass

    def set_status(self, status):
        self.status = status

    def get_account(self):
        pass

    def set_account(self):
        pass

    class Status(Enum):
        WAIT_VERSION = 0
        WAIT_PASSWORD = 1
        WAIT_ACCOUNT = 2
        WAIT_NICKNAME = 3
        SERVER = 4
