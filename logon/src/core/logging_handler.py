import logging
from time import strftime

from core.server_config import Config


class bcolors:
    blue = '\033[94m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    cend = '\033[0m'

class Logging:

    def __init__(self):
        logging.basicConfig(format="[%(levelname)s]%(message)s",
                                        filename="logon_master.log",
                                        level=logging.DEBUG)
        self.logger = logging.getLogger("Logon")
        conflevel = Config()
        conflevel.initialize()
        self.logger.setLevel(conflevel.get_loggin_level())

    def debug(self, message):
        if self.logger.getEffectiveLevel() <= 10:
            print(strftime("[%H:%M:%S]")+bcolors.green+'[DEBUG]'+bcolors.cend,message)
            logging.debug(strftime("[%d.%m][%H:%M:%S]")+message)

    def info(self, message):
        if self.logger.getEffectiveLevel() <= 20:
            print(strftime("[%H:%M:%S]")+bcolors.orange+'[INFO]'+bcolors.cend,message)
            logging.info(strftime("[%d.%m][%H:%M:%S]")+message)

    def warning(self, message):
        if self.logger.getEffectiveLevel() <= 30:
            print(strftime("[%H:%M:%S]")+bcolors.red+'[WARNING]'+bcolors.cend,message)
            logging.warning(strftime("[%d.%m][%H:%M:%S]")+message)
