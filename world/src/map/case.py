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

class Case:

    def __init__(self, map, id, walkable, loS, objId):
        # default values
        self.walkable = True
        self.walkableInFight = False
        self.loS = True

        self.id = id
        self.walkable = walkable
        self.walkableInFight = walkable
        self.loS = loS
        self.map = map.getId()
        if objId == -1:
            return
        # this.object = new InteractiveObject(objId, map, this);