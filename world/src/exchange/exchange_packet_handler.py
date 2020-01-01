from core.communication_service import CommunicationService
from core.logging_handler import Logging


class ExchangePacketHandler:

    def __init__(self):
        self.log = Logging()

    def parser(self, packet):
        if packet[0] == 'F':
            if packet[1] == '?': # F?
                # i = 50000 - Main.gameServer.getPlayerNumber()
                # exchangeClient.send("F" + i)
                return
            return
        elif packet[0] == 'S':
            if packet[1] == 'H': 
                if packet[2] == 'K': # SHK
                    self.log.debug('The login server validates the connection successfully.')
                    return
                return
            elif packet[1] == 'K':
                if packet[2] == '?': # SK?
                    self.log.debug('i = 50000 - Main.gameServer.getPlayerNumber()')
                    CommunicationService.exClient.send('SS0')
                    # i = 50000 - Main.gameServer.getPlayerNumber()
					# Main.exchangeClient.send("SK" + Main.serverId + ";" + Main.key + ";" + i)
                    return
                elif packet[2] == 'K': # SKK
                    # self.log.debug('The login server has accepted the connection')
					# Main.exchangeClient.send("SH" + Main.Ip + ";" + Main.gamePort)
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
