from os import system, name
import subprocess as sp
import time

class Console():

    def __init__(self):
        name = 'Cestra - Logon Server - '
        Version = '0.1'
        system('title '+name+Version)

    def clear(self):
        # for windows
        if name == 'nt':
            tmp = sp.call('cls',shell=True)

        # for mac and linux(here, os.name is 'posix')
        elif name == 'posix':
            tmp = sp.call('clear',shell=True)
