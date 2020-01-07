global ExClient

class CommunicationService:

    def __init__(self):
        pass

    def start_exClient(self, exCl):
        ExClient = CommunicationService.ExchangeClient(exCl)

    class ExchangeClient:

        def __init__(self, ioCon):
            self.ioConnector = ioCon

        def send(self, o):
            msg = bytes(o, 'utf-8')
            self.ioConnector.send(msg)