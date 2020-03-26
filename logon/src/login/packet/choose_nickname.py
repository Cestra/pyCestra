import re
from enum import Enum

from core.logging_handler import Logging
from dataSource.account_data import AccountData
from login.packet.account_queue import AccountQueue


class ChooseNickName:
    '''
    information material:
    https://www.dofus.com/en/mmorpg/community/nicknames#\n
    https://www.python-kurs.eu/re.php
    '''
    def __init__(self):
        self.log = Logging()

    def inspect(nickname):
        #                  Admin                    Modo                 GM           Game Master
        forbidden_words = [r'[Aa][Dd][Mm][Ii][Nn]', r'[Mm][Oo][Dd][Oo]', r'[Gg][Mm]', r'[Gg][Aa][Mm][Ee]-?[Mm][Aa][Ss][Tt][Ee][Rr]',]

        def forbidden_words_check(val):
            for x in forbidden_words:
                if re.search(x, nickname):
                    return False
            return True

        def forbidden_symbol(val):
            for i in nickname:
                nick = re.match(r'[a-z]?[A-Z]?[0-9]?\x2D?', i)
                if nick.group(0) == '':
                    return False
            return True

        flag = 0
        while True:
            # the nickname must be at least 3 symbol long
            if (len(nickname) < 3):
                flag = -1
                break
            # the nickname may only consist of a-z, A-Z, 0-1 and -
            elif not forbidden_symbol(nickname):
                flag = -1
                break
            # the nickname can not contain more than 4 "-"
            elif len(re.findall(r'\x2D', nickname)) >= 5:
                flag = -1
                break
            # the nickname can not contain more than 2 numbers
            elif len(re.findall(r'[0-9]', nickname)) >= 3:
                flag = -1
                break
            # The nickname can not be a forbidden word
            elif not forbidden_words_check(nickname):
                flag = -1
                break
            else:
                flag = 0
                return True
        if flag ==-1:
            return False

    def verify(self, client, nickname, accountDataDic):

        # test if the nickname of the account is empty
        account = client.get_account()
        if not account.get_nickname() == '':
            client.kick()
            return

        # nickname must be different from your username
        if nickname.lower() == account.get_name().lower():
            client.send("AlEr")
            return

        # the examination of the nickname string
        if not ChooseNickName.inspect(nickname):
            self.log.debug('[' + str(client.get_address()[0]) + ']'
                '[' + str(client.get_status().name) + '] This nickname is not available')
            # 'AlEs'= this nickname is not available.
            client.write("AlEs")
            return

        # is the nickname already taken?
        # AlEs = this nickname is not available.
        for i in accountDataDic:
            if i['nickname'] == nickname:
                self.log.debug('[' + str(client.get_address()[0]) + ']'
                                '[' + str(client.get_status().name) + ']' +
                                'This nickname is already in use')
                client.write("AlEs")
                return

        account.set_nickname(nickname)
        account.set_state(0)

        # set client status to SERVER
        client.set_status(Status(4))

        # update of the accountDataDic entry
        for i in accountDataDic:
            if i['id'] == account.get_id():
                i['nickname'] = account.get_nickname()
                break

        AccountQueue().verify(client, accountDataDic)


class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
