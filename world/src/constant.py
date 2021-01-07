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
from core.logging_handler import Logging

class Constant():

    def __init__(self):
        self.log = Logging()

    def get_start_map_incarnam(self, classID):
        ''' 
        Return [mapId(int), cellId(int)]\n
        Default: [10298,236]
        '''
        if classID == 1:
            return [10300,323]

        if classID == 2:
            return [10284,372]

        if classID == 3:
            return [10299,271]

        if classID == 4:
            return [10285,263]

        if classID == 5:
            return [10298,300]

        if classID == 6:
            return [10276,296]

        if classID == 7:
            return [10283,299]

        if classID == 8:
            return [10294,280]

        if classID == 9:
            return [10292,284]

        if classID == 10:
            return [10279,254]

        if classID == 11:
            return [10296,243]

        if classID == 12:
            return [10289,236]

        else:
            return [10298,236]
