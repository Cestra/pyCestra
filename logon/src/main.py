import sys
import os

from Database import Database
from PacketHandler import PacketHandler
from AccountData import AccountData
from ServerData import ServerData

if __name__ == "__main__":

    clear = lambda: os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)
    wel()

    def DBcheck():
        if Database().testConnection():
            print("Datenbank Connection Test Erfolgreich")
        else:
            print("Datanbank nicht gefunden!")
            sys.exit  

    # PacketHandler().TestSocket()
    DBcheck()
    
    print("### DATA TEST ###")
    test = ServerData(1).get()
    print(test)

    Account = AccountData(1).get()
    print(Account)