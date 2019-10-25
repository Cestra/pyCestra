import socket
from enum import Enum

from core.logging_handler import Logging
from src.login.packet.packet_handler import PacketHandler


class HelloConnection:
    
    def __init__(self, c, key, addr):
        self.log = Logging()
        self.log.debug('LoginClient created - '+ 
                        str(addr[0])+ ':'+ str(addr[1])+ ' - '+key)

        # Create the client instance
        Client = LoginClient()
        Client.set_key(key)
        Client.set_status(Status(0))
        Client.set_io_session(c)

        # We send the first package (HC + KEY + empty byte)
        token = bytes('HC'+key+'\x00', 'utf-8')
        self.log.debug("[SEND]: "+ str(token))
        c.send(token)

        # We are waiting for the client version
        data = c.recv(2048)
        msg = data.decode()
        if not msg == '1.29.1\n\x00':
            self.log.debug('Disconnected '+ str(addr[0])+ ':'+ str(addr[1]) +
                            'The client has the wrong version')
            f = bytes('AlEf'+'\x00', 'utf-8')
            c.send(f)
            c.close()
        self.log.debug('[' + str(addr[1]) + '][' + 
                        str(Client.get_status().name) + '] Version accepted')

        PacketHandler(Client)
        
        '''
        while True:
            data = c.recv(2048)
            if not data:
                break
            #msg = data.decode()
            print(data)
        '''

class LoginClient:

    def __init__(self):
        pass

    def send(self):
        pass

    def parser(self):
        pass

    def kick(self):
        print('KICK CLIENT')
        pass

    def get_id(self):
        pass

    def set_id(self, Client_id):
        self.id = Client_id

    def get_io_session(self):
        return self.setIoSession

    def set_io_session(self, session):
        self.set_io_session = session

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
