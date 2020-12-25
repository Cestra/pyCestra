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

import threading
import time

from core.logging_handler import Logging
from dataSource.DAO import DAO


class DatabaseUpdateService:

    def __init__(self):
        self.log = Logging()

    def start(self, accountDic, updateTime):
        threadName = 'Database-Update-Service'
        try:
            t = threading.Thread(target=DatabaseUpdateService.update_loop,
                                name=threadName,
                                args=(self, accountDic, updateTime))
            t.start()
            self.log.info('Database-Update-Service Successfully')
        except:
            self.log.warning('Database-Update-Service could not be created')

    def update_loop(self, accountDic, updateTime):

        def string_builder(i):
            queryPart = (
                'UPDATE `accounts` SET '
                '`pass` = \'{}\','
                '`rank` = \'{}\','
                '`nickname` = \'{}\','
                '`lastConnectionDate` = \'{}\','
                '`lastIP` = \'{}\','
                '`friends` = \'{}\','
                '`reload_needed` = \'{}\','
                '`logged` = \'{}\','
                '`subscribe` = \'{}\' '
                'WHERE (`id` = \'{}\');'.format(i["pass"],i["rank"],i["nickname"],
                                        i["lastConnectionDate"],
                                        i["lastIP"],i["friends"],i["reload_needed"],
                                        i["logged"],i["subscribe"],i["id"]))
            return queryPart

        dao = DAO()
        while True:
            time.sleep(updateTime)
            self.log.debug('[Database-Update-Service] - '
                            'Data is send to the database')
            start = time.time()
            counter = 0
            for i in accountDic:
                query = string_builder(i)
                dao.multi_update_data(query)
                del query
                counter = counter + 1
            ende = time.time()
            self.log.debug('[Database-Update-Service] - Data was transferred '
                            '(query:{}, total time: {:5.3f}s)'.format(counter, ende-start))
