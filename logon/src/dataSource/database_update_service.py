import threading
import time

from core.logging_handler import Logging
from dataSource.DAO import DAO


class DatabaseUpdateService():

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
        dao = DAO()
        while True:
            time.sleep(updateTime)
            self.log.debug('[Database-Update-Service] - SAVE DATA')
            start = time.time()
            counter = 0
            for i in accountDic:
                query = DatabaseUpdateService.string_builder(i)
                dao.multi_update_data(query)
                counter = counter + 1
            ende = time.time()
            self.log.debug('[Database-Update-Service] - SAVE PROCESS '
                            'FINISHED (counter:{}, total time:{:5.3f}s)'.format(counter, ende-start))

    def string_builder(i):
        i = i[0]
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
