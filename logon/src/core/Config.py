import configparser

from core.logging_handler import Log


class Config:

    def __init__(self):
        self.log = Log()
        self.log.debug('[DEBUG] Config instance has been created')
        self.config = configparser.ConfigParser()
        self.loginIp = '127.0.0.1'
        self.loginPort = 478
        self.version = '1.29.1'
        self.host = '127.0.0.1'
        self.port = 3306
        self.name = 'cestra_logon'
        self.user = 'root'
        self.passwo = 'root'
        self.exchangeIp = '127.0.0.1'
        self.exchangePort = 451

    def create_default_logon_config(self):
        try:
            self.config['LogonServer Basic Settings'] = {
                'Logon_Server_Ip': '127.0.0.1',
                'Logon_Server_Port': '478',
                'Logon_Server_Version': '1.29.1'
            }
            self.config['LogonServer Database'] = {
                'logon_database_ip': '127.0.0.1',
                'logon_database_port': '3306',
                'logon_database_name': 'cestra_game',
                'logon_database_user': 'root',
                'logon_database_pass': 'fabio312'
            }
            self.config['RealmList Configuration'] = {
                'Network_RealmList_Ip': '127.0.0.1',
                'Network_RealmList_Port': '451'
            }
            with open('./logon.conf', 'w') as configfile:    # save
                self.config.write(configfile)
            return True
        except:
            return False

    def initialize(self):
        try:
            section01 = 'LogonServer Basic Settings'
            section02 = 'LogonServer Database'
            section03 = 'RealmList Configuration'
            self.config.read('./logon.conf')

            self.loginIp = self.config.get(section01, 'Logon_Server_Ip')
            self.loginPort = self.config.getint(section01, 'Logon_Server_Port')
            self.version = self.config.get(section01, 'Logon_Server_Version')

            self.host = self.config.get(section02, 'logon_database_ip')
            self.port = self.config.getint(section02, 'logon_database_port')
            self.name = self.config.get(section02, 'logon_database_name')
            self.user = self.config.get(section02, 'logon_database_user')
            self.passwo = self.config.get(section02, 'logon_database_pass')

            self.exchangeIp = self.config.get(section03, 'Network_RealmList_Ip')
            self.exchangePort = self.config.getint(section03, 'Network_RealmList_Port')
        except:
            self.log.warning('Config.initialize: Unreadable config or missing fields')

    def get_login_ip(self):
        return self.loginIp

    def get_login_port(self):
        return self.loginPort

    def get_version(self):
        return self.version

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_database_name(self):
        return self.name

    def get_user(self):
        return self.user

    def get_pass(self):
        return self.passwo

    def get_exchange_ip(self):
        return self.exchangeIp

    def get_exchange_port(self):
        return self.exchangePort
