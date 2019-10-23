import socket
import threading
from enum import Enum

from core.logging_handler import Logging


class LoginClient:

    def __init__(self, c, key, addr):
        self.log = Logging()
        self.log.debug('LoginClient created - '+ str(addr[0])+ ':'+ str(addr[1])+ ' - '+key)
        # TODO Set status !
        # We send the first package (HC + KEY + empty byte)
        message = bytes('HC'+key+'\x00', 'utf-8')
        self.log.debug("[SEND]: "+ str(message))
        c.send(message)
        data = c.recv(2048)
        # Test loop 
        packe_counter = 0
        while True:
            data = c.recv(2048)
            packe_counter += 1
            if not data:
                print('0 DATA')
                self.log.info('Disconnected '+ str(addr[0])+ ':'+ str(addr[1])+ ' - Total Packet: ' + str(packe_counter))
                break
            msg = data.decode()
            # Test Packet 'AlEf'
            # Text Box: "Access denied. Invalid login or password"
            if packe_counter == 3:
                f = bytes('AlEf'+'\x00', 'utf-8')
                c.send(f)
                self.log.debug('[SEND]> AlEf')
            self.log.debug('[' + str(addr[1]) + '][Status]: "'+ msg+ '"')
        c.close()

    def send(self):
        pass

    def parser(self):
        pass

    def kick(self):
        pass

    def get_id(self):
        pass

    def set_id(self, Client_id):
        self.id = Client_id

    def get_io_session(self):
        return self.setIoSession

    def set_io_session(self):
        pass

    def get_key(self):
        return self.setKey

    def set_key(self, key):
        self.setKey = key

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