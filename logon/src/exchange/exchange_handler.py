import random

from core.logging_handler import Logging
from exchange.exchange_client import ExchangeClient


class HelloExchangeClient():

    def __init__(self, socket, addr):
        exClient = ExchangeClient()
        exClient.set_id(0)
        exClient.set_io_session(socket)
        exClient.set_id(ExchangeHandler().generate_session_id())
        exClient.send('SK?')
        ExchangeHandler().recv_loop(exClient)

class ExchangeHandler():

    def __init__(self):
        self.log = Logging()

    def recv_loop(self, exClient):
        while True:
            data = exClient.get_io_session().recv(2048)
            packet = data.decode()
            packetPrint = packet.replace('\n', '[n]')
            self.log.debug('[' + str(exClient.get_id()) + ']' + 
                            '[<-EX-RECV] ' + packetPrint)
            if not data:
                self.log.debug('[SERVER-NAME] PacketLoop no data')
                exClient.kick()
                break
            ExchangeHandler().parse(exClient, packet)

    def generate_session_id(self):
        key = ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        while len(key) < 16:
            char = random.choice(alphabet)
            key += char
        return key

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
