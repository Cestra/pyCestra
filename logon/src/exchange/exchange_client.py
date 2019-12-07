from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self, socket, addr):
        self.log = Logging()
        print('ExchangeClient', addr)

    def kick(self):
        pass

    def get_id(self):
        pass

    def set_id(self):
        pass

    def parse(self, packet):
        if packet[0] == 'F': #F
            pass
        elif packet[0] == 'S':
            if packet[1] == 'H': #SH
                pass
            elif packet[1] == 'K': #SK
                pass
            elif packet[1] == 'S': #SS
                pass
        elif packet[0] == 'M':
            if packet[1] == 'P': #MP
                pass
            elif packet[1] == 'T': #MT
                pass
            elif packet[1] == 'D': #MD
                pass
            elif packet[1] == 'O': #MO
                pass
        else:
            self.log.debug('Packet undefined\n(' + packet + ')')
