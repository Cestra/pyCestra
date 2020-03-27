import os

try:
    path = os.path.abspath("./logon/src/main.py")
    command = 'python ' + path
    os.system(command)
except:
    print('LOGON MAIN.py kann nicht gestart werden')