from src import main
from src.login.login_client import LoginClient
from src.object.account import Account


class PacketHandler:

    def parser(self, client, packet):
        if client.getStatus() == LoginClient.Status.WAIT_VERSION:
            # client.setStatus WAIT_ACCOUNT
            pass
        elif  client.getStatus() == LoginClient.Status.WAIT_ACCOUNT:
            # verifyAccountName and verifyPassword
            # client.send("AlEf")
            pass
        elif  client.getStatus() == LoginClient.Status.WAIT_NICKNAME:
            # ChooseNickName.verify(client, packet)
            #
            pass
        elif  client.getStatus() == LoginClient.Status.SERVER:
            if packet[0:2] == 'AF':
                # FriendServerList.get(client, packet)
                pass
            elif packet[0:2] == 'AX':
                # ServerSelected.get(
                pass
            elif packet[0:2] == 'Af':
                # AccountQueue.verify(client);
                pass
            elif packet[0:2] == 'Ax':
                # ServerList.get(client)
                pass
            client.kick()
        client.kick()

    def verifyAccountName(self, client, name):
        try:
            #Account account =  Main.database.getAccountData().load(name.toLowerCase(), client)
            if account == 0:
                return False
            client.set_account(account)
            client.getAccount().setClient(client)
        except:
            return False
        if client.getAccount() == 0:
            return False
        client.set_status(LoginClient.Status.WAIT_PASSWORD)
        return True

    def verify_password(self, client, apass):
        if not decrypt_password(apass, client.getKey()).equals(client.getAccount().getPass()):
            return False
        client.set_status(LoginClient.Status.WAIT_PASSWORD)
        return True

    # this function is not finished
    #has no function in the specification
    def decrypt_password(self, apass, key):
        chain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        decrypted = ""
        for i in range(0, len(apass), 2):
            pass
