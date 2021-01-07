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

import socket

class DemoClient:

    def response(self, client):
        data = client.recv(2048)
        packet = data.decode()
        packet = packet.replace('\x00', '')
        # packetPrint = packet.replace('\n', '[n]')
        # print('>>> ' + packetPrint)
        return packet

    def send(self, client, o):
        msg = bytes(o+'\x00', 'utf-8')
        client.send(msg)
        # print('<<< ' + o.replace('\n', '[n]'))