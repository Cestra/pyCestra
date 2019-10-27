import socket
import threading
import time
from enum import Enum

from core.logging_handler import Logging


class PacketHandler:

    def __init__(self):
        self.log = Logging()
    
    def loop(self, client):
        while True:
            # if the session close, values are deleted
            if client.get_io_session() == False:
                del client
            # wait for packages
            else:
                data = client.get_io_session().recv(2048)
            packet = data.decode()
            packetLog = packet.replace('\n', '[]')
            self.log.debug('[' + str(client.get_address()[1]) + ']'
                            '[' + str(client.get_status().name) + '] '
                            + packetLog)
            if not data:
                self.log.debug('PacketLoop no data')
                break
            PacketHandler().parser(client, packet)

    def parser(self, client, packet):
        # client arrived here, the version has been checked
        if client.get_status().name == Status.WAIT_VERSION.name:
            client.set_status(Status(2))
            self.log.debug('[' + str(client.get_address()[1]) + ']'
                            '[' + str(client.get_status().name) + '] Status change')

        if  client.get_status().name == Status.WAIT_ACCOUNT.name:
            #if not (verify_account_name) and (verify_password):
            if not PacketHandler().verify_password(client, packet.split('\n')[1]):
                client.write('AlEf')
            return

        if  client.get_status().name == Status.WAIT_NICKNAME.name:
            # ChooseNickName.verify(client, packet)
            #
            pass

        if  client.get_status().name == Status.SERVER.name:
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
    '''
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
    '''

    def verify_password(self, client, apass):
        print()
        # hier bin ich !
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

class Status(Enum):
    WAIT_VERSION = 0
    WAIT_PASSWORD = 1
    WAIT_ACCOUNT = 2
    WAIT_NICKNAME = 3
    SERVER = 4
