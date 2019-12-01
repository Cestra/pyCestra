import socket
import threading

from core.logging_handler import Logging


class ExchangeServer():

    def __init__(self):
        self.log = Logging()

    def start(self, ip, port):
        threadName = 'Exchange-Server - ' + str(port)
        try:
            t = threading.Thread(target=ExchangeServer.server,
                                name=threadName,
                                args=(self, ip, port))
            t.start()
        except:
            self.log.warning('Exchange Server could not be created')

    def server(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ip, port))
            self.log.debug('Exchange Socket binded to post: ' + str(port))
        except socket.error:
            self.log.warning('Exchange Socket - Binding faild')
        s.listen()
        self.log.info('Exchange Socket is listening')
        while True:
            c, self.addr = s.accept()
            # self.log.info('Connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            # LoginHandler().session_created(c, self.addr)
        s.close()
