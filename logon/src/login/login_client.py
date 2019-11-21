import sys
from enum import Enum

from core.logging_handler import Logging
from .packet.packet_handler import PacketHandler


class HelloConnection:

    def __init__(self, c, key, addr):
        self.log = Logging()

        # Create the client instance
        client = LoginClient()
        client.set_key(key)
        client.set_address(addr)
        client.set_status(Status(0))
        client.set_io_session(c)

        self.log.debug('[' + str(addr[0]) + '][' +
                        str(client.get_status().name) + '] Client created - '+key)

        # We send the first package (HC + KEY + empty byte)
        client.write('HC'+key)

        # We are waiting for the client version
        data = c.recv(2048)
        msg = data.decode()
        if not (msg == '1.30.0\n\x00' or msg == '1.29.1\n\x00'):
            self.log.debug('[' + str(addr[0]) + ']' +
                    '[' + str(client.get_status().name) +
                    '] The client has the wrong version')
            # TODO wrong text window is displayed "Invalid login or password."
            client.write('AlEf')
            sys.exit()
        self.log.debug('[' + str(addr[0]) + '][' +
                        str(client.get_status().name) + '] Version accepted')

        PacketHandler().loop(client)

class LoginClient:

    def __init__(self):
        self.log = Logging()

    def write(self, o):
        msg = bytes(o+'\x00', 'utf-8')
        self.log.debug('[' + str(self.address[0]) + ']'
                    '[' + str(self.status.name) + '][SEND->] ' + o)
        self.IoSession.send(msg)

    def parser(self):
        pass

    def kick(self):
        self.log.info('[' + str(self.address[0]) + ']'
                    '[' + str(self.status.name) + '] Client kick')
        sys.exit()

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
