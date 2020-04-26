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

import progressbar

import dataSource
from core.logging_handler import Logging
from client.player import Player
from dataSource.DAO import DAO


class PlayersData(DAO):

    def __init__(self):
        self.log = Logging()

    def load_in_to_class(self):
        '''
        DataFrame:

        '''
        self.dataSource = []
        connection = dataSource.Database().get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM players;')
            data = cursor.fetchall()
            for result in data:
                # the attributes are the inGame order
                stats = [result['vitality'], result['wisdom'], result['strength'],
                        result['intelligence'], result['chance'], result['agility']]
                player = Player(result['id'], result['name'], result['account'], result['group'],
                                result['sexe'], result['class'], result['color1'], result['color2'],
                                result['color3'], result['kamas'], result['spellboost'], result['capital'],
                                result['energy'], result['level'], result['xp'], result['size'],
                                result['gfx'], result['alignement'], result['honor'], result['deshonor'],
                                result['alvl'], stats, result['seeFriend'], result['seeAlign'],
                                result['seeSeller'], result['channel'], result['map'], result['cell'],
                                result['pdvper'], result['spells'], result['objets'], result['storeObjets'],
                                result['savepos'], result['zaaps'], result['jobs'], result['mountxpgive'],
                                result['title'], result['wife'], result['morphMode'], result['emotes'],
                                result['prison'], result['server'], result['logged'], result['allTitle'],
                                result['parcho'], result['timeDeblo'], result['noall'],)
                self.dataSource.append(player)
                return self.dataSource
        except Exception as Error:
            self.log.warning('player_data.py - Can\'t load table player')
            self.log.warning(str(Error))
        finally:
            cursor.close()
            connection.close()

    def get_player_data(self):
        return self.dataSource
