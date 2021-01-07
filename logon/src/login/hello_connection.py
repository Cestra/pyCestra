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
import re

from core.logging_handler import Logging


class HelloConnection():

    def __init__(self, c, ipbans):
        self.log = Logging()
        client = c
        # We send the first package (HC + KEY + empty byte)
        client.write('HC'+client.get_key())

        # We are waiting for the client version
        data = client.get_io_session().recv(2048)
        msg = data.decode()
        vc = re.search(r"1.[2-3][0-9].", msg)
        if not vc:
            self.log.debug('[' + str(client.get_address()[0]) +
                            ':' + str(client.get_address()[1]) +
                            '][' + str(client.get_status().name) +
                            '] The client has the wrong version - ' +
                            '(' + str(msg.split('\n')[0]) + ')')
            # TODO wrong text window is displayed "Invalid login or password."
            client.write('AlEf')
            sys.exit(0)
        for i in ipbans:
            if client.get_address()[0] == i['ip']:
                self.log.debug('[' + str(client.get_address()[0]) + ':' +
                                str(client.get_address()[1]) + ']' +
                                '[' + str(client.get_status().name) + '] ' +
                                'This IP is banned')
                client.write('AlEb')
                client.kick()
        self.log.debug('[' + str(client.get_address()[0]) + ':' +
                        str(client.get_address()[1]) +'][' +
                        str(client.get_status().name) + '] Version accepted ' +
                        '(' + str(msg.split('\n')[0]) + ')')
        return
