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

from core.logging_handler import Logging


class ServerList:
    '''
        AxK +
        subscribe(in millisecond) +
        server.getId() +
        number of characters

    client.write('AxK2628000000|1,4')
    '''
    def __init__(self):
        self.log = Logging()

    def get_list(self, client):
        client.write("AxK" + ServerList().server_list(client.get_account()))

    def server_list(self, account):
        return str(account.get_subscribe()) + '|1,2'

    def character_number(self):
        pass
