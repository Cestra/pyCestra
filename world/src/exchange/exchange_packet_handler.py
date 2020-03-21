from core.logging_handler import Logging


class ExchangePacketHandler:

    def __init__(self):
        self.log = Logging()

    def parser(self, packet, exClient):
        if packet[0] == 'F':
            if packet[1] == '?': # F?
                # i = 50000 - Main.gameServer.getPlayerNumber()
                # exchangeClient.send("F" + i)
                return
            return
        elif packet[0] == 'S':
            if packet[1] == 'H':
                if packet[2] == 'K': # SHK
                    self.log.debug('The Logon-Server validates the connection successfully.')
                    return
                return
            elif packet[1] == 'K':
                if packet[2] == '?': # SK?
                    i = 50000 - 0 # Main.gameServer.getPlayerNumber()
					# TODO Main.exchangeClient.send("SK" + Main.serverId + ";" + Main.key + ";" + i)
                    ExchangePacketHandler().send(exClient,'SK1;1;' + str(i))
                    return
                elif packet[2] == 'K': # SKK
                    self.log.debug('The Logon-Server has accepted the connection')  
					# TODO Main.exchangeClient.send("SH" + Main.Ip + ";" + Main.gamePort)
                    ExchangePacketHandler().send(exClient,'SH' + '127.0.0.1' + ';' + '5555')
                    return
                elif packet[2] == 'R': # SKR
					# self.log.debug('The login server refused the connection')
					# Main.stop()
                    return
                return
            return
        elif packet[0] == 'W':
            # if (packet.split("W").length > 2)
                # magic !
            if packet[1] == 'A': # WA
                return
            elif packet[1] == 'K': # WK
                return
            return
        elif packet[0] == 'M':
            if packet[1] == 'G': # MG
                return
            if packet[1] == 'F': # MF
                return
            if packet[1] == 'D': # MD
                return
            return

    def send(self, exClient, o):
        msg = bytes(o, 'utf-8')
        self.log.debug('[logon ip]' +
                '[EX-SEND->] ' + o)
        exClient.send(msg)
