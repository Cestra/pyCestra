import os
import threading
from typing_extensions import runtime

runtime = 30
name = ["logon-Server","world-Server","server-unittest"]

def lthread():
    try:
        t = threading.Thread(target=logonServer,name=name[0],args=runtime)
        t.start()
    except threading.ThreadError as e:
        print('Login Server could not be created: ' + str(e))

def logonServer():
    os.system('python logon/src/main.py')
    pass


/home/fabio/python/pyCestra/logon/src/main.py

testthread()