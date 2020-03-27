def decryptPassword(passs, key):
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

# Packet Inhalt: "AccountName#11ZQP77MN46 "
# Test 1 - gewünschtes Ergebnis: 12345
# print('decrypted: ' + decryptPassword('1ZQP77MN46','rgxcuzxlftyqdfyfvybwiseelgnfaqmr') + ' <- [12345]')

# Packet Inhalt: "admin[n]#1SN-8ahTW19[n] Af[n]"
# Test 2 - gewünschtes Ergebnis: admin
# print('decrypted: ' + decryptPassword('SN-8ahTW19','fxzgopoueppehteyixzzshavenlynqbz') + ' <- [admin]')

def encryptPassword(rawPass, key):
    Chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    encrypted = '#1'
    for i in range(len(rawPass)):
        loc6 = ord(rawPass[i])
        loc7 = ord(key[i])
        loc8 = loc6//16
        loc9 = loc6%16
        loc10 = Chaine[(loc8 + loc7 % len(Chaine)) % len(Chaine)]
        loc11 = Chaine[(loc9 + loc7 % len(Chaine)) % len(Chaine)]
        encrypted += loc10 + loc11
    return encrypted

print(45*'-')
print('encrypted: ' + encryptPassword('admin','fxzgopoueppehteyixzzshavenlynqbz') + ' <- [#1SN-8ahTW19]')
print(45*'-')