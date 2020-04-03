from core.logging_handler import Logging


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
                if s.get_sub() != 0 or s.get_free_places() > 0:
                    continue
                msg += str(s.get_id()) + '|'

        try:
            for i in hostList:
                if i.get_id() == packet:
                    server = i
            self.log.debug('[{}:{}][{}] Server {} has been selected'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name),
                                                                    packet))
            if server == None:
                self.log.debug('[{}:{}][{}] The selected server does not exist for the account'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name)))
                client.write('AXEr')
                return
            if server.get_status() != 1:
                self.log.debug('[{}:{}][{}] The status of the selected server is unavailable for the account'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name)))
                client.write('AXEd')
                return
            if account.is_subscribes() == False and server.get_sub() == 1:
                self.log.debug('[{}:{}][{}] The selected server is full or you must be subscribed for the account'.format(str(client.get_address()[0]),
                                                                                                                    str(client.get_address()[1]),
                                                                                                                    str(client.get_status().name)))
                client.write(get_free_server(hostList))
                return
            account.set_server(server.get_id())
            server.get_ex_client().send('WA{}'.format(str(account.get_id())))
            client.write('AYK{}:{};{}'.format(str(server.get_ex_client().get_addr()[0]),
                                        str(server.get_ex_client().get_addr()[1]),
                                        str(account.get_id())))
            account.set_state(0)
            self.log.debug('[{}:{}][{}] The test account has chosen its server well: the world-server takes over.'.format(str(client.get_address()[0]),
                                                                                                                    str(client.get_address()[1]),
                                                                                                                    str(client.get_status().name)))
        except:
            self.log.warning('[{}:{}][{}] The server selection failed'.format(str(client.get_address()[0]),
                                                                    str(client.get_address()[1]),
                                                                    str(client.get_status().name)))
            client.write('AXEr')
            client.kick()
            return
