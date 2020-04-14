'''
pyCestra - Open Source MMO Framework
Copyright (C) 2020 pyCestra Team

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

import sys

from core.logging_handler import Logging


class GameClient:

    def __init__(self, socket, addr):
        self.log = Logging()
        self.session = socket
        self.addr = addr
        # self.actions = 
        self.timeLastChatMsg = 0
        self.timeLastIncarnamMsg = 0
        self.timeLastAlignMsg = 0
        self.timeLastRecrutmentMsg = 0
        self.timeLastTradeMsg = 0
        self.walk = False
        self.waiter

    def kick(self):
        sys.exit(0)

    def get_session(self):
        return self.session

    def get_addr(self):
        return self.addr

    def set_character(self, character):
        self.character = character
    
    def get_character(self):
        return self.character