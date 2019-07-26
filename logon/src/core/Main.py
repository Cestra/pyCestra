import os
import sys

#import src.database
import database
# from PacketHandler import PacketHandler

if __name__ == "__main__":

    #  ======================================================
    #  start message

    def clear(): return os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - Logon Server   |", 31*"─"]
        for x in welmsg:
            print(x)
    wel()

    #  ======================================================
    #  Socket Tests

    # PacketHandler().test_socket()

    #  ======================================================
    #  MySQL Tests

    mySQLTest = database.Database()

    def database_test():
        print('Datenbank Connection Test:')
        if mySQLTest.test_connection():
            print('Datenbank Connection Test Erfolgreich')
        else:
            print('Datanbank nicht gefunden!')
            sys.exit

    database_test()

    print("### DATA TEST ###")
    Server = database.ServerData(1).get()
    print("Server Data Test:", Server)

    Account = database.AccountData(1).get()
    print("Account Data Test:", Account)

    Player = database.PlayerData(1).get()
    print("PlayerData Test:", Player)

    #  ======================================================
