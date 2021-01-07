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

import sys

from core.logging_handler import Logging


class ExchangeClient():

    def __init__(self):
        self.log = Logging()

    def send(self, i):
        msg = bytes(i, 'utf-8')
        self.log.debug('[{}:{}][EX-SEND->] {}'.format(str(self.addr[0]),
                                                str(self.addr[1]),
                                                i))               
        self.IoSession.send(msg)

    def kick(self):
        self.log.info('[{}:{}] Exchange Client has disconnected'.format(str(self.addr[0]),
                                                                str(self.addr[1])))
        sys.exit(0)

    def set_addr(self, addr):
        self.addr = addr

    def get_addr(self):
        return self.addr

    def get_id(self):
        return self.id

    def set_id(self, i):
        self.id = i

    def get_io_session(self):
        return self.IoSession

    def set_io_session(self, s):
        self.IoSession = s
