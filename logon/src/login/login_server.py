import socket
import threading

from core.logging_handler import Logging
from login.login_handler import LoginHandler


class LoginServer:

    def __init__(self):
        self.log = Logging()

    def start(self, ip, port, game_client_dic, ipbans):
        threadName = 'Login-Server - ' + str(port)
        try:
            t = threading.Thread(target=LoginServer.server,
                                name=threadName,
                                args=(self, ip, port, game_client_dic, ipbans))
            t.start()
        except threading.ThreadError as e:
            self.log.warning('Login Server could not be created: ' + str(e))

    def server(self, logon_ip, login_port, game_client_dic, ipbans):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((logon_ip, login_port))
        except socket.error:
            print('Binding faild')
        s.listen()
        self.log.info('Logon Socket is listening on Port: ' + str(login_port))
        while True:
            c, self.addr = s.accept()
            self.log.info('Connected '+ str(self.addr[0])+ ':'+ str(self.addr[1]))
            LoginHandler().session_created(c, self.addr, game_client_dic, ipbans)
        s.close()
