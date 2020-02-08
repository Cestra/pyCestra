from enum import Enum

from core.logging_handler import Logging


class AccountQueue:

    def __init__(self):
        self.log = Logging()

    def verify(self, client, game_client_dic):
        account = client.get_account()
        if account.is_banned() == 1:
            self.log.debug('[' + str(client.get_address()[0]) + ':' +
                            str(client.get_address()[1]) + ']' +
                            '[' + str(client.get_status().name) + '] ' +
                            'The account is banned')
            client.write('AlEb')
            client.kick()
            return

        # the ejection is not yet complete
        for game_client in game_client_dic.values():
            if not game_client.get_key() == client.get_key():
                dic_account = game_client.get_account()
                if dic_account.get_id() == account.get_id():
                    self.log.debug('[' + str(client.get_address()[0]) + ':' +
                                    str(client.get_address()[1]) + ']' +
                                    '[' + str(client.get_status().name) + '] ' +
                                    'this account is already logged in ...' +
                                    'the other session is now closed')
                    game_client.kick()

        AccountQueue().send_information(client,account)

    def send_information(self, client, account):
        if account.get_nickname() == '':
            client.write('AlEr')
            # set client status to WAIT_NICKNAME
            client.set_status(Status(3))
            self.log.debug('[' + str(client.get_address()[0]) + ':' +
                            str(client.get_address()[1]) + ']' +
                            '[' + str(client.get_status().name) + '] Status change')
            return
        self.log.debug('[' + str(client.get_address()[0]) + ':' +
                        str(client.get_address()[1]) + ']' +
                        '[' + str(client.get_status().name) + '] Sending account login information')
        # database.getPlayerData().load(account)
        client.write('Af0|0|0|1|-1')
        client.write('Ad' + account.get_nickname())
        client.write('Ac0')
        # -----------------------------------------
        # DEMO
        # client.write(Server.getHostList())
        client.write('AH127.0.0.1;1;110;1|')
        # -----------------------------------------
        client.write('AlK' + str(account.is_staff()))
        client.write('AQ' + account.get_question())

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
