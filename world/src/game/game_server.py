import socket
import threading

from core.logging_handler import Logging
from game.game_client import GameClient


class GameServer:

    def __init__(self):
        self.log = Logging()
        self.log.warning('GameServer instans !')

    def initialize(self, ip, port):
        threadName = 'Game-Server - ' + str(port)
        try:
            t = threading.Thread(target=GameServer.server,
                                name=threadName,
                                args=(self, ip, port))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Game Server could not be created' + str(e))

    def server(self, game_ip, game_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((game_ip, game_port))
        except socket.error:
            self.log.warning('Game Socket - Binding faild')
        s.listen()
        self.log.info('Game Socket is listening on Port: ' + str(game_port))
        while True:
            c, self.addr = s.accept()
            self.log.info('Connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            # XXXXXXXX.session_created(c, self.addr)
        s.close()

    def session_created(self, soecket, addr):
        threadName = 'Game-Client '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=GameClient,
                                name=threadName,
                                args=(soecket, addr,))
            t.start()
        except:
            self.log.warning('Game Client could not be created '+ str(addr[0])+':'+ str(addr[1]))
