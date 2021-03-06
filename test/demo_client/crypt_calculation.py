'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
