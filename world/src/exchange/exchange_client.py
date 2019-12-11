import socket
import time

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def test(self): # Demo Client
        HOST = '127.0.0.1'
        PORT = 451

        while True:
            time.sleep(5)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((HOST, PORT))
                self.log.debug('Connected to logon server')
                data = s.recv(1024)
                msg = data.decode()
                out = bytes('Hello, ' + msg  , 'utf-8')
                s.send(out)
                self.log.debug('Received: ' + str(msg))
            except:
                s.close()
                self.log.debug('...')
