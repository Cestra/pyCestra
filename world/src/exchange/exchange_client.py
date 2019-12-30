import socket
import sys
import threading

from core.logging_handler import Logging
from exchange.exchange_handler import ExchangeHandler


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def initialize(self, exchange_ip, exchange_port):
        try:
            exSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            exSocket.connect((exchange_ip, exchange_port))
            self.log.debug('Exchange-Client connected to logon server')
            self.ioConnector = exSocket
        except:
            exSocket.close()
            self.log.warning('It could not be connected to the login server')
            sys.exit(0)
        try:        
            exchangeHandler = ExchangeHandler()
            threadName = 'Exchange-Receiver - Port: '+str(exchange_port)
            t = threading.Thread(target=exchangeHandler.loop,
                                name=threadName,
                                args=(self.ioConnector,))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Exchange-Receiver could not be created ' + str(e))

    def send(self, o):
        msg = bytes(o, 'utf-8')
        self.ioConnector.send(msg)
