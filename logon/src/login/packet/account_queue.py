from core.logging_handler import Logging


class AccountQueue:

    def __init__(self):
        self.log = Logging()

    def verify(self, client):
        account = client.get_account()
        if account.is_banned() == 1:
            self.log.debug('[' + str(client.get_address()[1]) + ']'
                            '[' + str(client.get_status().name) + '] '
                            + 'The account is banned')
            client.write('AlEb')
            client.kick
            return
        print('send_information!')
        #AccountQueue().send_information(client,account)

    def send_information(self, client, account):
        print('send_information')
        '''
        if account == null
            log.DEBUG('The account does not exist. The client is kicked.')
            client.send('AlEb')
            client.kick
            return
        if account.getNickname.isEmpty()
            log.DEBUG('The'+account.getName()+' account does not have a nickname. '+
                    Send information to put nickname and nickname-status.')
            client.send('AlEr')
            client.setStatus(LoginClient.Status.WAIT_NICKNAME)
            return
        log.DEBUG('Sending account login information')
        database.getPlayerData().load(account);
        client.send('Af0|0|0|1|-1');
        client.send('Ad' + account.getPseudo());
        client.send('Ac0');
        client.send(Server.getHostList());
        client.send('AlK' + (account.isMj() ? 1 : 0));
        client.send('AQ' + account.getQuestion());
        '''
        pass
