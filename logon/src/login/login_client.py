import socket
import threading

from _thread import start_new_thread
from core.logging_handler import Logging

class LoginClient:

    # def __init__(self, c, key):
    def __init__(self, c):
        log = Logging()
        log.debug('LoginClient erstellt')

        # TODO bin dabei den key an die Klasse zu übergeben
        #LoginClient.get_key(key)

        message = 'HC/hjsuwdbsdialeghajbsnaheorhalehsq'
        c.send(message.encode('utf-8'))
        data = c.recv(1024)

        while True:
            c.send(message.encode('utf-8'))
            data = c.recv(1024)
            if not data:
                print('0 DATA')
                print('Disconnected ')
                # self.log.info('Disconnected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
                break
            # msg = data.decode()
            # print(self.addr[1], ': "', msg, '"')
        c.close()

    def send(self):
        pass

    def parser(self):
        pass

    def kick(self):
        pass

    def get_id(self):
        pass

    def set_id(self):
        pass

    def get_io_session(self):
        pass

    def get_key(self, key): return key

    def set_key(self):
        pass

    def get_status(self):
        pass

    def set_status(self):
        pass

    def get_account(self):
        pass

    def set_account(self):
        pass

    def status(self):
        pass
