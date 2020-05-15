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

class Account:

    def __init__(self, accId, nickname, question, reponse, subscribe, lastConnection, ip):
        self.accId = accId
        self.nickname = nickname
        self.question = question
        self.reponse = reponse
        self.subscribe = subscribe
        self.lastConnection = lastConnection
        self.ip = ip
        self.characters = {}
        self.charNum = 0

# ----------------------------------------

    def get_id(self):
        return self.accId

# ----------------------------------------

    def get_nickname(self):
        return self.nickname

# ----------------------------------------

    def get_question(self):
        return self.question

# ----------------------------------------

    def get_reponse(self):
        return self.reponse

# ----------------------------------------

    def get_subscribe(self):
        return self.subscribe

# ----------------------------------------

    def get_last_connection_date(self):
        return self.lastConnection

# ----------------------------------------

    def get_last_ip(self):
        return self.ip

# ----------------------------------------

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

# ----------------------------------------

    def get_game_client(self):
        return self.gameClient

    def set_game_client(self, gc):
        self.gameClient = gc

# ----------------------------------------

    def get_characters(self):
        return self.characters

    def set_characters(self, chrlist):
        self.set_number_of_characters(len(chrlist))
        self.characters = chrlist

# ----------------------------------------

    def get_number_of_characters(self):
        return self.charNum

    def set_number_of_characters(self, value):
        self.charNum = value

# ----------------------------------------

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = self.characters[player]

# ----------------------------------------