import sys
from PacketHandler import PacketHandler

if __name__ == "__main__":

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)

    wel()


    #Also TestServer() aus socketmanager startet jetzt über die main.py so
    #wie es soll aber des threadgin geht nicht
    PacketHandler()



    pass

    