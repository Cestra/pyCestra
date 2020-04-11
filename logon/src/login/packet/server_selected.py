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

from core.logging_handler import Logging
from login.packet.server_list import ServerList


class ServerSelected():

    def __init__(self, client, packet, hostList):
        self.log = Logging()
        account = client.get_account()
        packet = packet.replace('\n\x00', '')
        packet = int(packet)
        server = None

        def get_free_server(hostList):
            msg = 'AXEf'
            for s in hostList:
                try:
                    fp = s.get_free_places()
                except AttributeError:
                    fp = 0
                if s.get_sub() != 0 or fp > 0:
                    continue
                msg += str(s.get_id()) + '|'
                return msg
        
        try:
            # server is searched from the host list
            for i in hostList:
                if i.get_id() == packet:
                    server = i
            self.log.debug('[{}:{}][{}] Server {} has been selected'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name),
                                                                    packet))
            # client is kicked if this server id does not exist
            if server is None:
                self.log.debug('[{}:{}][{}] The selected server does not exist for the account'.format(str(client.get_address()[0]),
                                                                                                    str(client.get_address()[1]),
                                                                                                    str(client.get_status().name)))
                # clinet msg: You are not allowed to connect to this server.
                client.write('AXEr')
                return
            # the selected server is not in the correct status for the account
            if server.get_status() != 1:
                self.log.debug('[{}:{}][{}] The status of the selected server is unavailable for the account'.format(str(client.get_address()[0]),
                                                                                                                str(client.get_address()[1]),
                                                                                                                str(client.get_status().name)))
                # clinet msg: The server you selected is unavailable at this time.
                client.write('AXEd')
                return
            # the selected server is only available to subscribers
            if account.is_subscribes() == 0 and server.get_sub() == 1:
                self.log.debug('[{}:{}][{}] The selected server is full or you must be subscribed for the account'.format(str(client.get_address()[0]),
                                                                                                                    str(client.get_address()[1]),
                                                                                                                    str(client.get_status().name)))
                # clinet msg: Server:FULL Maximum number of players reached.
                #             To get priority access, please becomme a full member by subscribing..
                client.write(get_free_server(hostList))
                ServerList().get_list(client)
                return
            account.set_server(server.get_id())
            server.get_ex_client().send('WA{}'.format(str(account.get_id())))
            client.write('AYK{}:{};{}'.format(str(server.get_ip()),
                                        str(server.get_port()),
                                        str(account.get_id())))
            account.set_state(0)
            self.log.info('[{}:{}][{}] Client connects to World-Server:{}'.format(str(client.get_address()[0]),
                                                                                str(client.get_address()[1]),
                                                                                str(client.get_status().name),
                                                                                str(server.get_id())))
        except Exception as e:
            self.log.warning('[{}:{}][{}] The server selection failed\n{}'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name),
                                                                    e))
            client.write('AXEr')
            client.kick()
            return
