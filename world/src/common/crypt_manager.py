'''
pyCestra - Open Source MMO Framework
Copyright (C) 2020 pyCestra Team

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

class CryptManager:

    def __init__(self):
        pass
    
    def get_int_by_hashed_value(self, c):
        hash = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
				's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
				'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
				'8', '9', '-', '_')
        return hash[c]

    def decompile_map_data(self, map, dData):
        val1, val2 = 0, 10
        cells = {} # Integer, Case
        for _ in range(len(dData)//10):
            cellData = dData[val1:val2]
            cellInfosByteList

            my_str = "hello world"
            my_str_as_bytes = str.encode(my_str)
            type(my_str_as_bytes) # ensure it is byte representation

            val1 += 10
            val2 += 10

val1 = 'HhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaatTHhaaeaaatQHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaatQHhaaeaaaaaHhaaeaaaaaHhaaenfiaaH3bNengatUHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaatTHhaaeaaaaaHhbKeaaaaaHhaaenfiaaHNHLerraaaH3HLerrqaaHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhbKeaaaaaHhbKenfiaaHNbLerralhHhHJeaaaaaH3HLerrqaaHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhbKeaaaaaGhbKeaaeYWHNHLerraaaHhHJeaaaaaHhHJeaaaaaG3bLetfaaaHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhbKeaaaaaHNHLeaaaaaHhHJectaaaHhHOeaaaaaGhbJeb1aaaG3bLerzGCXHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaenfiaaHNHLerraaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaGhbJerrGCXG3bLeruaaaHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaenfiaaHNbLeteilgHhHJeaaaaaHhHJerAaaaHhHJeaaaaaHhHJerrGaaGhbJeruaCYH3HLerzqqKHhaaenfaaaHhbKeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaenfiaaHNHLerraqxHhHJeaaaaaHhHJerAaaaHhHJerBaaaHhHJerrGtmHhHJeruaaaHhHJerraaaH3bLerruvjHhbKenfaaaHhbKeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHNHNerzau_HhHJeaaaaaHhHJeaaaaaHhHJerAaaaHhHJetnaaaHhHJeruau_HhHJerzaaaHhHJeaaaaaH3HLerrqaaGhbKeaaaYWHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHJerrqaaHhHJeruaaaHhHJeaaaqwHhHJeaaaqwH3HLeaaaaaHhbKeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJecraaaHhHJeaaaaaHhHJeaaaaaHhHJerrqaaHhHJerraaaHhHJerBaaaHhHJeaaaaaH3HLerrqaaHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJemYaaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHJeLFaaaHhHJeaaaaaH3bLerruvjHhaaenfaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJeaaaaaHhHJeb1aaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHJeaaaaaHhHNerzGqKHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHOeaaaaaHhHJerBaaaHhHMeaaaaaHhHJeaaaaaHhHJeb8aaaHhHJeaaaaaHhHLerrGqKHhaaerravbHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJeaaaaaHhHLeaaaaaHxHMeb2aaaHhHJeaaaaaHhHJeaaaaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHLeaaaaaHNHLeaaaaaHhHJerAaaaHhHJethaaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHNerrWaaHNHLeaaaaaHhHJeaaaaaHhHJeaaaaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHNHNerrWaaHhHJeaaaaaHhHJemYaaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHJeaaaaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHLerrWaaHhHLerrGaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHxHNerzWaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaerrqaaHhaaerraaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaaHhaaeaaaaa'
val2 = 'test'
val3 = 4

# CryptManager().decompile_map_data(val2, val1)
print(CryptManager().get_int_by_hashed_value(val3))