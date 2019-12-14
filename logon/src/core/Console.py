from os import system, name 
import time

class Console():

    def __init__(self):
        name = 'Cestra - Logon Server - '
        Version = '0.1'
        system('title '+name+Version)

    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 
