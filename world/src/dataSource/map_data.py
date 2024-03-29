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

import dataSource
from core.logging_handler import Logging
from map.map import Map
from dataSource.DAO import DAO


class MapData(DAO):

    def __init__(self):
        self.log = Logging()

    def load_in_to_class(self):
        '''
        DataFrame:

        '''
        self.dataSource = {}
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM maps;')
            data = cursor.fetchall()
            c = 0
            for result in data:
                c += 1
                try:
                    mapData = Map(result['id'],result['date'],
                                result['width'],result['heigth'],
                                result['key'],result['places'],
                                result['mapData'],result['cells'],
                                result['monsters'],result['mappos'],
                                result['numgroup'],result['fixSize'],
                                result['minSize'],result['maxSize'],
                                result['cases'],result['forbidden'],)
                    self.log.onlyShow('----- Maps are initialized: {} out of {} -----'.format(str(c), str(len(data))))
                    self.dataSource[result['id']] = mapData
                except Exception as Error:
                    self.log.warning('maps_data.py - maps:{} can\'t be loaded'.format(str(result['id'])))
                    self.log.warning(Error)
        except Exception as Error:
            self.log.warning('map_data.py - Can\'t load table accounts')
            self.log.warning(str(Error))
        finally:
            cursor.close()
            connection.close()

    def get_map_data(self):
        return self.dataSource
