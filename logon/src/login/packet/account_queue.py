class AccountQueue:

    def verify(self, client):
        '''
        if isBanned
            client.send('AlEb')
            client.kick
        sendInformation(client,account);
        '''
        pass

    def send_information(self, client, account):
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
