import random
import threading
from enum import Enum

from core.logging_handler import Logging
from login.hello_connection import HelloConnection
from login.login_client import LoginClient
from login.packet.packet_handler import PacketHandler


class LoginHandler:

    def __init__(self):
        self.log = Logging()

    def login(self, soecket ,key ,addr, game_client_dic):
        client = LoginClient(game_client_dic)
        client.set_key(key)
        client.set_address(addr)
        client.set_status(Status(0))
        client.set_io_session(soecket)

        self.log.debug('[' + str(addr[0]) + ':' + str(addr[1]) + '][' +
                        str(client.get_status().name) + '] Client created - '+key)

        # the object is save in the global dictionary 
        dict_str = addr[0] + ':' + str(addr[1])
        game_client_dic[dict_str] = client

        HelloConnection(client)
        LoginHandler().recv_loop(client, game_client_dic)

    def recv_loop(self, client, game_client_dic):
        while True:
            data = client.get_io_session().recv(2048)
            packet = data.decode()
            packetPrint = packet.replace('\n', '[n]')
            self.log.debug('[' + str(client.get_address()[0]) + ':' +
                            str(client.get_address()[1]) + ']' +
                            '[' + str(client.get_status().name) + '][<-RECV] ' +
                            packetPrint)
            if not data:
                self.log.debug('[' + str(client.get_address()[0]) + ':' +
                            str(client.get_address()[1]) + ']' +
                            '[' + str(client.get_status().name) + '] PacketLoop no data')
                client.kick()
                break
            PacketHandler().parser(client, packet, game_client_dic)

    def session_created(self, soecket, addr, game_client_dic):
        key = LoginHandler.generate_key(0)
        threadName = 'Client-Session '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=LoginHandler.login,
                                name=threadName,
                                args=(self, soecket, key, addr, game_client_dic))
            t.start()
        except threading.ThreadError as e:
            self.log.debug('Created Session '+ str(addr[0])+':'+ str(addr[1]) + ': ' + str(e))

    def session_opened(self):
        pass

    def send_to_all(self):
        pass

    def generate_key(self):
        key = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        while len(key) < 32:
            char = random.choice(alphabet)
            key += char
        # key = key[:-1]
        return key

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
