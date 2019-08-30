import random
import string

import threading
from core.logging_handler import Logging
from login.login_client import LoginClient


class LoginHandler:

    def __init__(self):
        self.log = Logging()

    def exception_caught(self):
        pass

    def message_received(self):
        pass

    def message_sent(self):
        pass

    def session_closed(self):
        pass

    def session_created(self, soecket, addr):
        key = LoginHandler.generate_key(0)
        threadName = 'Client-Session '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=LoginClient,
                                name=threadName,
                                args=(soecket, key, addr,))
            t.start()
        except:
            self.log.debug('Created Session '+ str(addr[0])+':'+ str(addr[1]))

    def session_idle(self):
        pass

    def session_opened(self):
        pass

    def send_to_all(self):
        pass

    def generate_key(self):
        key = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        while len(key) < 32:
            char = random.choice(alphabet)
            key += char
        # key = key[:-1]
        return key

    def input_closed(self):
        pass
