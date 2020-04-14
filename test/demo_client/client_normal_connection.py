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

import socket

from demo_client.crypt_calculation import Crypt


class DemoClient01:

    def start(self, account, password):

        def response():
            data = client.recv(2048)
            packet = data.decode()
            packet = packet.replace('\x00', '')
            packetPrint = packet.replace('\n', '[n]')
            print('>>> ' + packetPrint)
            return packet

        def send(o):
            msg = bytes(o+'\x00', 'utf-8')
            client.send(msg)
            print('<<< ' + o.replace('\n', '[n]'))

        result_dic = {}

        # ----------------------
        # test 01 connection
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 55020))
            result_dic["test_connection"] = True
        except Exception:
            result_dic["test_connection"] = False
        # ----------------------
        # # key response
        key = response()
        if len(key) == 34 and type(key) is str:
            result_dic["test_key_response"] = True
        else:
            result_dic["test_key_response"] = False
        # # ----------------------
        # # version und account send
        send('1.29.1\n')
        dp = Crypt().encryptPassword(password, key[2:])
        send(account + '\n' + dp + '\n Af\n')
        # # ----------------------
        # Af0|0|0|1|-1
        packet = response()
        if packet == 'Af0|0|0|1|-1':
            result_dic["test_packet_01"] = True
        else:
            result_dic["test_packet_01"] = False
        # # ----------------------
        # unittest-01
        packet = response()
        if packet == 'Aduni-one':
            result_dic["test_packet_02"] = True
        else:
            result_dic["test_packet_02"] = False
        # # ----------------------
        # Ac0
        packet = response()
        if packet == 'Ac0':
            result_dic["test_packet_03"] = True
        else:
            result_dic["test_packet_03"] = False
        # # ----------------------
        # AH
        packet = response()
        if packet[:2] == 'AH':
            result_dic["test_packet_04"] = True
        else:
            result_dic["test_packet_04"] = False
        # # ----------------------
        # AlK0      
        packet = response()
        if packet == 'AlK0':
            result_dic["test_packet_05"] = True
        else:
            result_dic["test_packet_05"] = False
        # # ----------------------
        # AQDELETE?
        packet = response()
        if packet == 'AQDELETE?':
            result_dic["test_packet_06"] = True
        else:
            result_dic["test_packet_06"] = False
        # # ----------------------
        # Ax[n]
        send('Ax[n]')
        # # ----------------------
        # AxK0|0,0
        packet = response()
        if packet == 'AxK0|0,0':
            result_dic["test_packet_07"] = True
        else:
            result_dic["test_packet_07"] = False
        # # ----------------------
        # test ende
        send('')
        client.close()

        return result_dic
