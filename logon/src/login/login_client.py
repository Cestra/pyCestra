import base64
import socket
import threading
from enum import Enum

from core.logging_handler import Logging


class LoginClient:

    def __init__(self, c, key, addr):
        self.log = Logging()
        self.log.debug('LoginClient created - '+ str(addr[0])+ ':'+ str(addr[1])+ ' - '+key)
        a = None
        message = bytes('\x4c\xcc\x6a\x89\xb4\x63\x38\x10\xd5\x1a\x32\xd7\x08\x00\x45\x00' +
                        '\x00\x4b\xc0\x12\x40\x00\x2a\x06\x4e\x49\x22\xfb\xac\x8b\xc0\xa8' +
                        '\xb2\x22\x15\xb3\xec\x0c\x9b\x8f\xa6\x77\x6c\x37\x1e\x0b\x50\x18' +
                        '\x00\x35\xb6\x2f\x00\x00\x48\x43\x6b\x77\x70\x68\x69\x76\x65\x73' +
                        '\x69\x63\x6c\x6a\x68\x6d\x66\x6c\x6a\x65\x75\x6d\x63\x64\x71\x63' +
                        '\x62\x6a\x6f\x63\x67\x69\x63\x63\x00', 'utf-8')
        print('len = ', len(message),' = ', message)

        c.send(message)
        data = c.recv(2048)
        test = repr(data)
        print(test)

        '''
        msg = data.decode()
        self.log.debug(str(addr[1])+ ': "'+ msg+ '"')
        
        while True:
            c.send(message.encode('utf-8'))
            self.log.debug("[SEND]: "+message)
            data = c.recv(2048)
            if not data:
                print('0 DATA')
                self.log.info('Disconnected '+ str(addr[0])+ ':'+ str(addr[1]))
                break
            msg = data.decode()
            self.log.debug(str(addr[1])+ ': "'+ msg+ '"')
        print('hey')
        c.close()
        '''

    def send(self):
        pass

    def parser(self):
        pass

    def kick(self):
        pass

    def get_id(self):
        pass

    def set_id(self, id):
        ip = self.id

    def get_io_session(self):
        return self.setIoSession

    def set_io_session(self):
        pass

    def get_key(self):
        return self.setKey

    def set_key(self, key):
        key = self.setKey

    def get_status(self):
        return self.status

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