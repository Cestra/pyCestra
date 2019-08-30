from src.login.login_client import LoginClient
from src.object.account import Account
from src import main

class PacketHandler:

    def parser(self, client, packet):
        if client.getStatus() == LoginClient.Status.WAIT_VERSION:
            pass
        elif  client.getStatus() == LoginClient.Status.WAIT_VERSION:
            pass
        elif  client.getStatus() == LoginClient.Status.WAIT_VERSION:
            pass
        elif  client.getStatus() == LoginClient.Status.WAIT_VERSION:
            if packet[0:2] == 'AF':
                pass
            elif packet[0:2] == 'AX':
                pass
            elif packet[0:2] == 'Af':
                pass
            elif packet[0:2] == 'Ax':
                pass
            elif packet[0:2] == 'Ax':
                pass
            client.kick()
        client.kick()
    
    '''
    def verifyAccountName(self, client, name):
        try:
            #Account account =  Main.database.getAccountData().load(name.toLowerCase(), client)
            if account == null:
                return False
            ckient.set_account(account)
            client.getAccount().setClient(client)
        except:
            return False
        if client.getAccount() == null:
            return False
        client.set_status(LoginClient.Status.WAIT_PASSWORD)
        return True

    def verify_password(self, client, apass):
        if not decrypt_password(apass, client.getKey()).equals(client.getAccount().getPass()):
            return False
        client.set_status(LoginClient.Status.WAIT_PASSWORD)
        return True

    def decrypt_password(self, apass, key):
        chain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        decrypted = ""
        for i in range(0, len(apass), 2):
            pass
    '''
