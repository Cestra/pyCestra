from core.logging_handler import Logging
from dataSource.DAO import DAO


class IpBans(DAO):

    def __init__(self):
        self.log = Logging()

    def load(self):
        self.data = super().get_data('SELECT * FROM ipbans;')
        return self.data
