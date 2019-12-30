from core.logging_handler import Logging


class ExchangeHandler:
     
    def __init__(self):
        self.log = Logging()

    def loop(self, exSocket):
        self.log.debug('Exchange-Receiver is started')
        # out = bytes('Hallo', 'utf-8')
        # exSocket.send(out)
        while True:
            data = exSocket.recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[logon ip][<-EX-RECV] '
                            + packetLog)
            if not data:
                self.log.debug('[logon ip] PacketLoop no data')
                # kick
                break
            ExchangePacketHandler.parse(packet)
