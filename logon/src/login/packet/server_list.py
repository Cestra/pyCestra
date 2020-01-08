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
        return '0|0,0'

    def character_number(self):
        pass
