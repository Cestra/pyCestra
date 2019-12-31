import sys

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def send(self, i):
        msg = bytes(i, 'utf-8')
        self.log.debug('[' + str(self.id) + ']' +
                        '[EX-SEND->] ' + i)
        self.IoSession.send(msg)

    def kick(self):
        self.log.info('[SERVER-NAME] Exchange Client has disconnected')
        sys.exit(0)

    def get_id(self):
        return self.id

    def set_id(self, i):
        self.id = i

    def get_io_session(self):
        return self.IoSession

    def set_io_session(self, s):
        self.IoSession = s
