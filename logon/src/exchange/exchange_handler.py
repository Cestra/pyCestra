import random

from core.logging_handler import Logging
from exchange.exchange_client import ExchangeClient


class HelloExchangeClient():

    def __init__(self, socket, addr, host_list_dic):
        exClient = ExchangeClient(host_list_dic)
        exClient.set_io_session(socket)
        exClient.set_addr(addr)
        exClient.set_id(ExchangeHandler().generate_session_id())

        # the object is save in the global Host-List
        dict_str = str(addr[0]) + ':' + str(addr[1]) + ':' + str(exClient.get_id())
        host_list_dic[dict_str] = exClient

        exClient.send('SK?')
        ExchangeHandler().recv_loop(exClient)

class ExchangeHandler():

    def __init__(self):
        self.log = Logging()

    def recv_loop(self, exClient):
        while True:
            try:
                data = exClient.get_io_session().recv(2048)
            except ConnectionResetError:
                exClient.kick()
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
            return
        elif packet[0] == 'S':
            if packet[1] == 'H': #SH
                s = packet[2:].split(';')
                ip = str(s[0])
                port = int(s[1])
                # TODO set State 1
                exClient.send('SHK')
                return
            elif packet[1] == 'K': #SK
                s = packet[2:].split(';')
                id = int(s[0])
                key = str(s[1])
                freePlaces = int(s[2])
                self.log.warning('save somehow !')
                # TODO
                # if (!server.getKey().equals(key)) {
                    # send("SKR")
                    # kick()
                exClient.send('SKK')
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
