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
import random


class NameGenerator:
    def __init__(self):
        self.vokal = ['a','e','i','o','u','ei','ie','au','eu']
        self.konsonant = ['b','d','f','g','h','j','k','l','m','n',
                        'p','q','r','s','t','v','w','x','z','y','ch',
                        'sch','pf','qu','sp','st','ll','pp','tt']
        self.matrix = self.syllableMatrix()

    def __del__(self):
        del self.vokal
        del self.konsonant
        del self.matrix

    def syllableMatrix(self):
        matrix = []
        for k in self.konsonant:
            row = []
            for v in self.vokal:
                syllable = k + v
                row.append(syllable)
            matrix.append(row)
        for k in self.konsonant:
            row = []
            for v in self.vokal:
                syllable = v + k
                row.append(syllable)
            matrix.append(row)
        return matrix

    def generator(self):
        nameLen = random.randint(2, 3)
        name = ''
        for _ in range(nameLen):
            column = random.randint(1, len(self.vokal)) - 1
            row = random.randint(1, len(self.konsonant)) - 1
            syllable = self.matrix[row][column]
            name += syllable
            if name[0] == name[1]:
                name = name[1:]
        return name.capitalize()

    def get_name(self):
        name = self.generator()
        if random.choice([True, False, False]):
            extra = self.generator()
            name += '-' + extra
        return name

name = NameGenerator()
for _ in range(0,15):
    print(name.get_name())
del name