import sys

from core.logging_handler import Logging


class HelloExchangeClient():

    def __init__(self, socket, addr):
        exClient = ExchangeClient()
        exClient.set_id(0)
        exClient.set_io_session(socket)
        # exClient.send('Cesta')
        ExchangeLoop().loop(exClient)

class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def send(self, i):
        msg = bytes(i, 'utf-8')
        self.log.debug('[SERVER-NAME][EX-SEND->] ' + i)
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

class ExchangeLoop():

    def __init__(self):
        self.log = Logging()

    def loop(self, exClient):
        while True:
            data = exClient.get_io_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[SERVER-NAME][<-EX-RECV] '
                            + packetLog)
            if not data:
                self.log.debug('[SERVER-NAME] PacketLoop no data')
                exClient.kick()
                break
            ExchangeLoop().parse(exClient, packet)

    def parse(self, exClient, packet):
        if packet[0] == 'F': #F
            # org.cestra.exchange.ExchangePacketHandler @ parser
            # F + getPlayerNumber
            pass
        elif packet[0] == 'S':
            if packet[1] == 'H': #SH
                pass
            elif packet[1] == 'K': #SK
                pass
            elif packet[1] == 'S': #SS
                # org.cestra.game.GameServer @ setState
                # SS0 SS1 SS2
                pass
        elif packet[0] == 'M':
            if packet[1] == 'P': #MP
                # org.cestra.game.GameClient @ parseMigration
                # MP + GameClient.this.compte.getGuid
                pass
            elif packet[1] == 'T': #MT
                # org.cestra.exchange.ExchangePacketHandler @ parser
                # MT" + account + "|" + server
                pass
            elif packet[1] == 'D': #MD
                pass
            elif packet[1] == 'O': #MO
                # org.cestra.game.GameClient @ parseMigration
                # MO + split[0] + "|" + server2
                pass
        self.log.warning('Packet undefined: ' + packet)
        exClient.kick()
