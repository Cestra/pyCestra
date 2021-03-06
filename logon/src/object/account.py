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

import datetime

class Account():

    def __init__(self):
        self.isSub = 0

# ----------------------------------------

    def get_id(self):
        return self.UUid
    
    def set_id(self, i):
        self.UUid = i

# ----------------------------------------
    
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name = n
# ----------------------------------------

    def get_pass(self):
        return self.passs

    def set_pass(self, p):
        self.passs = p

# ----------------------------------------

    def get_nickname(self):
        return self.nickname

    def set_nickname(self, ni):
        self.nickname = ni

# ----------------------------------------

    def get_question(self):
        return self.question
    
    def set_question(self, q):
        self.question = q

# ----------------------------------------

    def get_reponse(self):
        return self.reponse
    
    def set_reponse(self, r):
        self.reponse = r

# ----------------------------------------

    def get_state(self):
        return self.state

    def set_state(self, s): # "logged" byte
        self.state = s

# ----------------------------------------
 
    def is_staff(self):
        return self.staff

    def set_staff(self, staff):
        self.staff = staff

# ----------------------------------------

    def get_client(self):
        return self.client

    def set_client(self, client):
        self.client = client

# ----------------------------------------

    def get_server(self):
        return self.server

    def set_server(self, server):
        self.server = server

# ----------------------------------------

    def get_subscribe_remaining(self):
        pass

# ----------------------------------------

    def get_subscribe(self):
        return self.subscribe

    def set_subscribe(self, sup):
        if sup == 0 or sup == '0':
            self.subscribe = sup
        else:
            # ----------------------------------------
            # current time
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M")
            # ----------------------------------------
            n = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M')
            s = datetime.datetime.strptime(sup, '%Y-%m-%d %H:%M')
            # ----------------------------------------
            # value = subscription - now
            v = s - n
            # ----------------------------------------
            # value in milliseconds
            x = (v.days * 24 * 60 * 60 * 1000) + (v.seconds * 1000)
            # ----------------------------------------
            # the subscribe is in the past ?
            if x < 0:
                self.subscribe = 0
                self.isSub = 0
            else:
                self.subscribe = x
                self.isSub = 1
            # ----------------------------------------

    def is_subscribes(self):
        return self.isSub

# ----------------------------------------

    def set_banned(self, b):
        self.banned = b

    def is_banned(self):
        return self.banned

# ----------------------------------------

    def add_player(self):
        pass

    def del_player(self):
        pass

    def get_players(self):
        pass
