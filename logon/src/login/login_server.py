import socket
import sys
import threading

from core.logging_handler import Logging
from core.server_config import Config
from login.login_handler import LoginHandler


class LoginServer:

    def __init__(self):
        self.log = Logging()

    def start(self, logon_ip, login_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((logon_ip, login_port))
            self.log.info('Logon Socket binded to post: ' + str(login_port))
        except socket.error:
            print('Binding faild')
        s.listen()
        self.log.info('Logon Socket is listening')
        while True:
            c, self.addr = s.accept()
            self.log.info('Connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            LoginHandler().session_created(c, self.addr)
        s.close()

    def stop(self):
        pass

    def get_clients(self, session):
        pass
