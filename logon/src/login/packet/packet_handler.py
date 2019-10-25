from src import main
from src.login.login_client import LoginClient,Status
from src.object.account import Account


class PacketHandler:

    def __init__(self, client):
        while True:
            data = c.recv(2048)
            if not data:
                 self.log.debug('')
            print(data)

    def parser(self, client, packet):
        if client.get_status().name == 'WAIT_VERSION':
            client.set_status(Status('WAIT_ACCOUNT'))
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

    def decrypt_password(self, passs, key):
        Chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        decrypted = ""
        for i in range(len(passs)//2):
            PKey = ord(key[i])
            ANB = Chaine.index(passs[i*2])
            ANB2 = Chaine.index(passs[i*2+1])
            somme1 = ANB + len(Chaine)
            somme2 = ANB2 + len(Chaine)
            APass = somme1 - PKey
            if APass < 0:
                APass += 64
            APass *= 16
            AKey = somme2 - PKey
            if AKey < 0:
                AKey += 64
            PPass = chr(APass + AKey)
            decrypted = decrypted + PPass
        return decrypted
