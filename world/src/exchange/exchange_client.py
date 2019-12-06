import socket
import time

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self):
        self.log = Logging

    def test(self):
        HOST = '127.0.0.1'
        PORT = 451

        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((HOST, PORT))
                print('wir sind drin')
                s.send(b'Hello, world')
                data = s.recv(1024)
                print('Received', repr(data))
            except:
                s.close()
                print('warten...')
                time.sleep(2.5)
