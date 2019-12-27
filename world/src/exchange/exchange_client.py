import socket
import threading

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def initialize(self, ip, port):
        threadName = 'Exchange-Client - ' + str(port)
        try:
            t = threading.Thread(target=ExchangeClient.client,
                                name=threadName,
                                args=(self, ip, port))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Exchange-Client could not be created: ' + str(e))

    def client(self, game_ip, game_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            self.log.debug('Connected to logon server')
            # data = s.recv(1024)
            # msg = data.decode()
            # out = bytes('Hello, ' + msg  , 'utf-8')
            # s.send(out)
            # self.log.debug('Received: ' + str(msg))

        except:
            s.close()
            self.log.info('ExchangeClient - Try to connect..')
