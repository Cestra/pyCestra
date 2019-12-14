import threading

from core.logging_handler import Logging
from game.game_client import GameClient


class GameHandler:

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
                gameClient.kick()
                break
            # XXXXXXXX.parse(gameClient, packet)

    def session_created(self, soecket, addr):
        threadName = 'Game-Client '+str(addr[0])+':'+ str(addr[1])
        try:
            t = threading.Thread(target=GameClient,
                                name=threadName,
                                args=(soecket, addr,))
            t.start()
        except:
            self.log.warning('Game Client could not be created '+ str(addr[0])+':'+ str(addr[1]))
