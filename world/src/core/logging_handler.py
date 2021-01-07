'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import logging
from time import strftime

from core.server_config import Config


class bcolors:
    blue = '\033[94m'
    #red = '\033[31m'
    red = '\33[41m'
    green = '\033[32m'
    orange = '\033[33m'
    cend = '\033[0m'

class Logging:

    def __init__(self):
        logging.basicConfig(format="[%(levelname)s]%(message)s",
                                        filename="world_master.log",
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
            print(strftime(bcolors.red+"[%H:%M:%S]")+'[WARNING]',message+bcolors.cend)
            logging.warning(strftime("[%d.%m][%H:%M:%S]")+message)
