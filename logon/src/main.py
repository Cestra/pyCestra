import sys
from PacketHandler import PacketHandler
from Database import Database

if __name__ == "__main__":

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)

    wel()
    
    # PacketHandler().TestSocket()

    if Database().testConnetcion() == True:
        print("testConnetcion Erfolgreich")
    else:
        print("GEHT NICHT")

    pass