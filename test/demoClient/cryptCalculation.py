class Crypt:

    def encryptPassword(self, rawPass, key):
        _Chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        _encrypted = '#1'
        for i in range(len(rawPass)):
            _loc6 = ord(rawPass[i])
            _loc7 = ord(key[i])
            _loc8 = _loc6//16
            _loc9 = _loc6%16
            _loc10 = _Chaine[(_loc8 + _loc7 % len(_Chaine)) % len(_Chaine)]
            _loc11 = _Chaine[(_loc9 + _loc7 % len(_Chaine)) % len(_Chaine)]
            _encrypted += _loc10 + _loc11
        return _encrypted
