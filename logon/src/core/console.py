from os import system, name
import subprocess as sp

class Console:

    def __init__(self):
        name = 'Cestra - Logon Server - '
        Version = '0.1'
        system('title '+name+Version)

    def clear(self):
        # for windows
        if name == 'nt':
            sp.call('cls',shell=True)

        # for mac and linux (here, os.name is 'posix')
        elif name == 'posix':
            sp.call('clear',shell=True)
