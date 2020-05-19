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

class Map():

    def __init__(self, id, date, width, heigth, key, places, mapData, cells,
                monsters, mapPos, numGroup, fixSize, minSize, maxSize, cases, forbidden):
        self.id = id
        self.data = date
        self.width = width
        self.heigth = heigth
        self.key = key
        self.places = places
        self.mapData = mapData
        self.cells = cells
        self.monsters = monsters
        self.numGroup = numGroup
        self.fixSize = fixSize
        self.minSize = minSize
        self.maxSize = maxSize
        self.cases = cases
        self.forbidden = forbidden

        try:
            mapPos.split(',')
            self.X = mapPos[0]
            self.Y = mapPos[1]
        except Exception as Error:
            print('Map.__init__ {}'.format(Error))
