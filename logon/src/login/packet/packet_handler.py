from enum import Enum

from core.logging_handler import Logging
from dataSource.account_data import AccountData


class PacketHandler:

    def __init__(self):
        self.log = Logging()

    def loop(self, client):
        while True:
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
            # set client status to WAIT_ACCOUNT
            client.set_status(Status(2))
            self.log.debug('[' + str(client.get_address()[1]) + ']'
                            '[' + str(client.get_status().name) + '] Status change')

        if  client.get_status().name == Status.WAIT_ACCOUNT.name:
            verifyAccountName = PacketHandler().verify_account_name(client, packet.split('\n')[0])
            verifyPassword = PacketHandler().verify_password(client, packet.split('\n')[1])
            if not (verifyAccountName and verifyPassword):
                self.log.debug('[' + str(client.get_address()[1]) + ']'
                        '[' + str(client.get_status().name) + '] Login credentials incorrect')
                client.write('AlEf')

        if  client.get_status().name == Status.WAIT_NICKNAME.name:
            # ChooseNickName.verify(client, packet);
            print('WAIT_NICKNAME')

        if  client.get_status().name == Status.SERVER.name:
            if (packet[0:2] == 'AF') or (packet.split('\n')[2][1:] == 'AF'):
                # FriendServerList.get(client, packet)
                print('packet[0:2] == AF:')
            elif (packet[0:2] == 'AX') or (packet.split('\n')[2][1:] == 'AX'):
                # ServerSelected.get(
                print('packet[0:2] == AX:')
            elif (packet[0:2] == 'Af') or (packet.split('\n')[2][1:] == 'Af'):
                # AccountQueue.verify(client);
                print('packet[0:2] == Af:')
            elif (packet[0:2] == 'Ax') or (packet.split('\n')[2][1:] == 'Ax'):
                # ServerList.get(client)
                print('packet[0:2] == Ax:')
                # ServerList.get(client)
            client.kick()
        client.kick()

    def verify_account_name(self, client, name):
        try:
            account = AccountData().get_from_name(name)
            # check if the tuple is empty
            if not account:
                return False
            client.set_account(account)
            # client.getAccount().setClient(client)
        except AttributeError as err:
            print(err)
            return False
        # set client status to WAIT_PASSWORD
        client.set_status(Status(1))
        self.log.debug('[' + str(client.get_address()[1]) + ']'
                        '[' + str(client.get_status().name) + '] Status change')
        return True


    def verify_password(self, client, password):
        c = client.get_account()[0]
        if not PacketHandler().decrypt_password(password[2:], client.get_key()) == c['pass']:
            return False
        # set client status to SERVER
        client.set_status(Status(4))
        self.log.debug('[' + str(client.get_address()[1]) + ']'
                        '[' + str(client.get_status().name) + '] Status change')
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
