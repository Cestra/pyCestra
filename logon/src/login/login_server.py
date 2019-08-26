import socket
import sys
import threading

from _thread import start_new_thread
from core.logging_handler import Logging
from core.server_config import Config


class LoginServer:

    def __init__(self):
        self.log = Logging()

    def client_thread(self, c): 
        print('1')
        # ding = "AlEf"
        c.send("AlEf".encode())
        while True:
            print('2')
            # c.send(ding.encode())
            # data received from client 
            data = c.recv(1024)
            print('3')
            if not data:
                self.log.info('Disconnected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
                break
            print('4')
            msg = data.decode()
            print(self.addr[1], ': "', msg, '"')
        # connection closed 
        c.close()

    def start(self, logon_ip, login_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((logon_ip, login_port))
            self.log.info('Logon Socket binded to post: ' + str(login_port))
        except socket.error:
            print('Binding faild')
            sys.exit
        s.listen()
        self.log.info('Logon Socket is listening')
        while True:
            c, self.addr = s.accept()
            self.log.info('Connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            start_new_thread(self.client_thread, (c,))
        s.close()

    def stop(self):
        pass

    def get_clients(self, session):
        pass
