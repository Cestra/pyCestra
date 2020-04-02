import socket
import threading

from core.logging_handler import Logging
from exchange.exchange_handler import HelloExchangeClient


class ExchangeServer():

    def __init__(self):
        self.log = Logging()

    def start(self, ip, port, hostList):
        threadName = 'Exchange-Server - ' + str(port)
        try:
            t = threading.Thread(target=ExchangeServer.server,
                                name=threadName,
                                args=(self, ip, port, hostList))
            t.start()
        except:
            self.log.warning('Exchange Server could not be created')

    def server(self, ex_ip, ex_port, hostList):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ex_ip, ex_port))
        except socket.error:
            self.log.warning('Exchange Socket - Binding faild')
        s.listen()
        self.log.info('Exchange Socket is listening on Port: ' + str(ex_port))
        while True:
            c, self.addr = s.accept()
            self.log.info('Exchange Client connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            ExchangeServer().session_created(c, self.addr, hostList)
        s.close()

    def session_created(self, soecket, addr, hostList):
        threadName = 'Exchange-Client '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=HelloExchangeClient,
                                name=threadName,
                                args=(soecket, addr, hostList))
            t.start()
        except:
            self.log.warning('Exchange Client could not be created '+ str(addr[0])+':'+ str(addr[1]))
