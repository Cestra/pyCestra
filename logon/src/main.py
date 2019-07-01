import sys
import os
import database

# from database.Database import Database
from PacketHandler import PacketHandler
# from database.AccountData import AccountData
# from database.ServerData import ServerData

if __name__ == "__main__":

    #  ======================================================
    #  start message

    clear = lambda: os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)
    wel()

    #  ======================================================
    #  Socket Tests

    # PacketHandler().TestSocket()

    #  ======================================================
    #  MySQL Tests

    mySQLTest = database.Database()

    def DatabaseTest():
        if mySQLTest.testConnection():
            print("Datenbank Connection Test Erfolgreich")
        else:
            print("Datanbank nicht gefunden!")
            sys.exit  

    DatabaseTest()

    '''
    print("### DATA TEST ###")
    Server = ServerData(1).get()
    print("Server Data Test:", Server)

    Account = AccountData(1).get()
    print("Account Data Test:", Account)
    '''
    #  ======================================================