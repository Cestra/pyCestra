import sys

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self, host_list_dic):
        self.host_list_dic = host_list_dic
        self.log = Logging()

    def send(self, i):
        msg = bytes(i, 'utf-8')
        self.log.debug('[' + str(self.id) + ']' +
                        '[EX-SEND->] ' + i)
        self.IoSession.send(msg)

    def kick(self):
        dict_str = str(self.addr[0]) + ':' + str(self.addr[1]) + ':' + str(self.id)
        try:
            self.host_list_dic.pop(dict_str)
        except KeyError:
            self.log.warning('[' + str(self.id[0]) + ']' +       
                            '] The request in "host_list_dic" has been incorrectly removed')
        self.log.info('[' + str(self.id) + '] Exchange Client has disconnected')
        sys.exit(0)

    def set_addr(self, addr):
        self.addr = addr
    
    def get_addr(self):
        return self.addr

    def get_id(self):
        return self.id

    def set_id(self, i):
        self.id = i

    def get_io_session(self):
        return self.IoSession

    def set_io_session(self, s):
        self.IoSession = s
