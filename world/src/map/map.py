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

    def __init__(self, mapId, date, width, heigth, key, places, mapData, cells,
                monsters, mapPos, numGroup, fixSize, minSize, maxSize, cases, forbidden):
        print(str(mapId), 'Map')
        self.id = mapId
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
        self.forbiddenCellSpawn = cases
        # -----------------------------------------
        # if (!places.equalsIgnoreCase("") && !places.equalsIgnoreCase("|")) {
        #     final String[] split = places.split("\\|");
        #     this.maxTeam0 = split[0].length() / 2;
        #     this.maxTeam1 = split[1].length() / 2;
        # }
        # -----------------------------------------
        try:
            mapPos.split(',')
            self.X = mapPos[0]
            self.Y = mapPos[1]
            del mapPos
        except Exception as Error:
            print('Map.__init__ {}'.format(Error))
        # -----------------------------------------
        # subArea
        # -----------------------------------------
        try:
            split = forbidden.split(';')
            self.noTrader = split[0] in '1'
            self.noCollector = split[1] in '1'
            self.noPrism = split[2] in '1'
            self.noTP = split[3] in '1'
            self.noDefie = split[4] in '1'
            self.noAgro = split[5] in '1'
            self.noChannel = split[6] in '1'
            del forbidden, split
        except Exception as Error:
            print('Map.__init__ {}'.format(Error))
        # -----------------------------------------
        # if
        #     this.cases = CryptManager.decompileMapData(this, dData)
        # else:
        #     final String[] cellsDataArray = cellsData.split("\\|");
		# 	String[] array;
		# 	for (int length = (array = cellsDataArray).length, j = 0; j < length; ++j) {
		# 		final String o = array[j];
		# 		boolean Walkable = true;
        #         ...
        #         ...
        #         ...
        # -----------------------------------------
        # String[] split2;
		# for (int length2 = (split2 = monsters.split("\\|")).length, k = 0; k < length2; ++k) {
		# 	final String mob = split2[k];
        # -----------------------------------------
        # if (!cases.isEmpty()) {
        #             for (final Case c : this.cases.values()) {
        #                 c.setWalkableInFight(false);
        #             }
        #             try {
        #                 String[] split3;
        #                 ....
        #                 ....
        #                 ....
        # -----------------------------------------