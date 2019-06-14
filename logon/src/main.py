import sys
from PacketHandler import PacketHandler

if __name__ == "__main__":

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)

    wel()
    
    PacketHandler().TestSocket()

    pass