import os
import socket
import time
import unittest

class DemoClient:

    def __init__(self):
            print('DEMO CLIENT')

    def start(self, account, password):

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

        result_dic = {}

        # ----------------------
        # test 01 connection
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 55020))
            result_dic["test_connection"] = True
        except Exception:
            result_dic["test_connection"] = False
        # ----------------------
        # # key response
        key = response()
        if len(key) == 34 and type(key) is str:
            result_dic["test_key_response"] = True
        else:
            result_dic["test_key_response"] = False
        time.sleep(0.2)
        # # ----------------------
        # # version und account send
        send('1.29.1\n')
        dp = decrypt_password(password, key)
        send(account + '\n' + dp + '\n Af\n')
        client.close()
        # # ----------------------
        # response()
        # time.sleep(0.2)
        # # ----------------------
        # response()
        # time.sleep(0.2)
        # # ----------------------
        # response()
        # time.sleep(0.2)
        # # ----------------------
        # response()
        # time.sleep(0.2)
        # # ----------------------
        # client.close()
        # print(10*'-')

        return result_dic