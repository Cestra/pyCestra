from core.logging_handler import Logging


class ExchangeHandler:
     
    def __init__(self):
        self.log = Logging()

    def loop(self, gameClient):
        while True:
            data = gameClient.get_io_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[TODO client ip][<-EX-RECV] '
                            + packetLog)
            if not data:
                self.log.debug('[TODO client ip] PacketLoop no data')
                # kick
                break
            ExchangePacketHandler.parse(packet)
