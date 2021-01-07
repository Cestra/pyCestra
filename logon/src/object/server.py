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

class Server():
    '''
    int id;
    int port;
    int state;
    int pop;
    int sub;
    int freePlaces;
    String ip;
    String key;
    ExchangeClient client;
    public static Map<Integer, Server> servers;
    '''

    def __init__(self, id, key, status, pop, subscribe):
        self.id = id
        self.key = key
        self.status = status
        self.pop = pop
        self.sub = subscribe

# ----------------------------------------

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

# ----------------------------------------

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

# ----------------------------------------

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

# ----------------------------------------

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

# ----------------------------------------

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

# ----------------------------------------

    def get_pop(self):
        return self.pop

    def set_pop(self, pop):
        self.pop = pop

# ----------------------------------------

    def get_sub(self):
        return self.sub

    def set_sub(self, sub):
        self.sub = sub

# ----------------------------------------

    def get_ex_client(self):
        return self.exClient

    def set_ex_client(self, client):
        self.exClient = client

# ----------------------------------------

    def get_free_places(self):
        return self.freePlaces

    def set_free_places(self, freePlaces):
        self.freePlaces = freePlaces

# ----------------------------------------

    # Server Map

    def send(self):
        pass

    def send_host_list_to_all(self):
        pass