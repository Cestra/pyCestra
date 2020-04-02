import sys
import time

from core.logging_handler import Logging
from dataSource.DAO import DAO


class MapData(DAO):

    def __init__(self):
        self.log = Logging()

    def pre_Load(self):
        mapdata = super().pre_load('SELECT * FROM maps;')
        print(mapdata[5])

    def get_account_data(self):
        return self.Datasource

    def single_update(self, acc_id, valueTyp, value):
        '''
        acc_id
        valueTyp = Column name as in the database
        value

        example:
        update(1,'logged','1')
        '''
        data = 'UPDATE `accounts` SET `{}` = \'{}\' WHERE (`id` = \'{}\');'.format(str(valueTyp),str(value),str(acc_id))
        super().update_data(data)
