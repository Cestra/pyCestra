import random

from core.logging_handler import Logging
from exchange.exchange_client import ExchangeClient


class HelloExchangeClient():

    def __init__(self, socket, addr, hostList):
        exClient = ExchangeClient()
        exClient.set_io_session(socket)
        exClient.set_addr(addr)
        exClient.send('SK?')
        ExchangeHandler().recv_loop(exClient, hostList)

class ExchangeHandler():

    def __init__(self):
        self.log = Logging()

    def recv_loop(self, exClient, hostList):
        while True:
            try:
                data = exClient.get_io_session().recv(2048)
            except ConnectionResetError:
                exClient.kick()
            packet = data.decode()
            packetPrint = packet.replace('\n', '[n]')
            self.log.debug('[{}:{}][<-EX-RECV] {}'.format(str(exClient.get_addr()[0]),
                                                    str(exClient.get_addr()[1]),
                                                    packetPrint))            
            if not data:
                self.log.debug('[SERVER-NAME] PacketLoop no data')
                exClient.kick()
                break
            ExchangeHandler().parse(exClient, packet, hostList)

    def parse(self, exClient, packet, hostList):
        if packet[0] == 'F': #F
            # org.cestra.exchange.ExchangePacketHandler @ parser
            # F + getPlayerNumber
            return
        elif packet[0] == 'S':
            if packet[1] == 'H': #SH
                # SH Ip ; Port
                s = packet[2:].split(';')
                ip = str(s[0])
                port = int(s[1])
                for i in hostList:
                    if exClient.get_id() == i.get_id():
                        i.set_status(1)
                self.log.debug('[{}:{}] Status to 1'.format(str(exClient.get_addr()[0]),
                                                    str(exClient.get_addr()[1])))
                exClient.send('SHK')
                return
            elif packet[1] == 'K': #SK
                # 'SK id; key; freePlaces'
                s = packet[2:].split(';')
                id = int(s[0])
                key = str(s[1])
                freePlaces = int(s[2])
                exClient.set_id(id)
                for i in hostList:
                    if i.get_key() == key:
                        i.set_ex_client(exClient)
                        exClient.send('SKK')
                        break
                    else:
                        exClient.send('SKR')
                        exClient.kick()
                return
            elif packet[1] == 'S': #SS
                # org.cestra.game.GameServer @ setState
                # SS0 SS1 SS2
                return
        elif packet[0] == 'M':
            if packet[1] == 'P': #MP
                # org.cestra.game.GameClient @ parseMigration
                # MP + GameClient.this.compte.getGuid
                return
            elif packet[1] == 'T': #MT
                # org.cestra.exchange.ExchangePacketHandler @ parser
                # MT" + account + "|" + server
                return
            elif packet[1] == 'D': #MD
                return
            elif packet[1] == 'O': #MO
                # org.cestra.game.GameClient @ parseMigration
                # MO + split[0] + "|" + server2
                return
        self.log.warning('[' + str(exClient.get_id()) + '] Packet undefined: ' + packet)
        exClient.kick()
