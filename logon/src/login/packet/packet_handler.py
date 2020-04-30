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

from enum import Enum

from core.logging_handler import Logging
from login.packet.account_queue import AccountQueue
from login.packet.choose_nickname import ChooseNickName
from login.packet.server_list import ServerList
from login.packet.server_selected import ServerSelected
from object.account import Account


class PacketHandler:

    def __init__(self):
        self.log = Logging()

    def parser(self, client, packet, game_client_dic, accountDataDic, hostList):
        self.client = client
        # self.client arrived here, the version has been checked
        if self.client.get_status().name == Status.WAIT_VERSION.name:
            # set self.client status to WAIT_ACCOUNT
            self.client.set_status(Status(2))
            self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                            str(self.client.get_address()[1]) + ']' +
                            '[' + str(self.client.get_status().name) + '] Status change')

        if  self.client.get_status().name == Status.WAIT_ACCOUNT.name:
            verifyAccountName = self.verify_account_name(packet.split('\n')[0], accountDataDic)
            verifyPassword = self.verify_password(packet.split('\n')[1])
            if not (verifyAccountName and verifyPassword):
                self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                            str(self.client.get_address()[1]) + ']' +
                            '[' + str(self.client.get_status().name) + '] Login credentials incorrect')
                self.client.write('AlEf')

        if  self.client.get_status().name == Status.WAIT_NICKNAME.name:
            ChooseNickName().verify(self.client, packet[:-2], accountDataDic, hostList)
            return

        if  self.client.get_status().name == Status.SERVER.name:
            if (packet[0:2] == 'AF') or (packet[-4:-2] == 'AF'):
                # FriendServerList.get(self.client, packet)
                print('packet[0:2] == AF:')
            elif (packet[0:2] == 'AX') or (packet[-4:-2] == 'AX'):
                ServerSelected(self.client, packet[2:], accountDataDic, hostList)
            elif (packet[0:2] == 'Af') or (packet[-4:-2] == 'Af'):
                account = self.client.get_account()
                for game_client in game_client_dic.values():
                    if not game_client.get_key() == self.client.get_key():
                        dic_account = game_client.get_account()
                        if dic_account.get_id() == account.get_id():
                            self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                                            str(self.client.get_address()[1]) + ']' +
                                            '[' + str(self.client.get_status().name) + '] ' +
                                            'this account is already logged in ...' +
                                            'the other session is now closed')
                            game_client.kick()
                AccountQueue().verify(self.client, accountDataDic, hostList)
                return

            elif (packet[0:2] == 'Ax') or (packet[-4:-2] == 'Ax'):
                ServerList().get_list(self.client)
                return
            return

            self.client.kick()
        self.client.kick()

    def verify_account_name(self, name, accountDataDic):
        # accountDataDic is checked whether the account exists
        def load_from_result_set(resultSet):
            account = Account()
            account.set_id(resultSet['id'])
            account.set_name(resultSet['account'])
            account.set_pass(resultSet['pass'])
            account.set_nickname(resultSet['nickname'])
            account.set_question(resultSet['question'])
            account.set_reponse(resultSet['reponse'])
            account.set_state(resultSet['logged'])
            account.set_subscribe(resultSet['subscribe'])
            account.set_banned(resultSet['banned'])
            account.set_staff(resultSet['rank'])
            return account

        for i in accountDataDic:
            if i['account'] == name:
                account = load_from_result_set(i)
                self.client.set_account(account)
                break
            else:
                account = 0
                self.client.set_account(account)

        if account == 0:
            return False
        self.client.get_account().set_client(self.client)
        # set self.client status to WAIT_PASSWORD
        self.client.set_status(Status(1))
        self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                        str(self.client.get_address()[1]) + ']' +
                        '[' + str(self.client.get_status().name) + '] Status change')
        return True

    def verify_password(self, password):
        account = self.client.get_account()
        if account == 0:
            return False
        if not self.decrypt_password(password[2:], self.client.get_key()) == account.get_pass():
            return False
        # set self.client status to SERVER
        self.client.set_status(Status(4))
        self.log.debug('[' + str(self.client.get_address()[0]) + ':' +
                        str(self.client.get_address()[1]) + ']' +
                        '[' + str(self.client.get_status().name) + '] Status change')
        return True

    def decrypt_password(self, passs, key):
        _Chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        _decrypted = ""
        for i in range(len(passs)//2):
            _PKey = ord(key[i])
            _ANB = _Chaine.index(passs[i*2])
            _ANB2 = _Chaine.index(passs[i*2+1])
            _somme1 = _ANB + len(_Chaine)
            _somme2 = _ANB2 + len(_Chaine)
            _APass = _somme1 - _PKey
            if _APass < 0:
                _APass += 64
            _APass *= 16
            _AKey = _somme2 - _PKey
            if _AKey < 0:
                _AKey += 64
            _PPass = chr(_APass + _AKey)
            _decrypted = _decrypted + _PPass
        return _decrypted

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
