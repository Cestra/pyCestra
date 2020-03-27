import os
import socket
import time

def decrypt_password(passs, key):
    Chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    decrypted = ""
    for i in range(len(passs)//2):
        PKey = ord(key[i])
        ANB = Chaine.index(passs[i*2])
        ANB2 = Chaine.index(passs[i*2+1])
        somme1 = ANB + len(Chaine)
        somme2 = ANB2 + len(Chaine)
        APass = somme1 - PKey
        if APass < 0:
            APass += 64
        APass *= 16
        AKey = somme2 - PKey
        if AKey < 0:
            AKey += 64
        PPass = chr(APass + AKey)
        decrypted = decrypted + PPass
    return decrypted

def response():
    data = client.recv(2048)
    packet = data.decode()
    packet = packet.replace('\x00', '')
    packetPrint = packet.replace('\n', '[n]')
    print('>>> ' + packetPrint)
    return packet

def send(o):
    msg = bytes(o+'\x00', 'utf-8')
    client.send(msg)
    print('<<< ' + o.replace('\n', '[n]'))

# ----------------------
# test 01 connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if not client.connect(('127.0.0.1', 55020)):
    test01 = 0
test01 = 1
# ----------------------

account = 'admin'
password = 'admin'

print(10*'-')
# ----------------------
# key response
key = response()
time.sleep(0.2)
# ----------------------
# version und account send
send('1.29.1\n')
dp = decrypt_password(password, key)
print(dp)

send(account + '\n' + dp + '\n Af\n')
# ----------------------
response()
time.sleep(0.2)
# ----------------------
response()
time.sleep(0.2)
# ----------------------
response()
time.sleep(0.2)
# ----------------------
response()
time.sleep(0.2)
# ----------------------
client.close()
print(10*'-')