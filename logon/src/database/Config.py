import configparser

class Config:

    def __init__(self):
        print('[DEBUG] Config instance has been created')

    def createDefault(self):
        self.config = configparser.ConfigParser()
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
        self.config = configparser.ConfigParser()
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
            print('[ERROR] Config.initialize: Unreadable config or missing fields')

    def getLoginIp(self):
        return self.loginIp

    def getLoginPort(self):
        return self.loginPort

    def getVersion(self):
        return self.version

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def getDatabaseName(self):
        return self.name

    def getUser(self):
        return self.user

    def getPass(self):
        return self.passwo

    def getExchangeIp(self):
        return self.exchangeIp

    def getExchangePort(self):
        return self.exchangePort

# Config().createDefault()
# DbConfig = Config()
# print(type(DbConfig.get()))
# print(DbConfig.get())
# data = DbConfig.get()
# print(data['ip'])
'''
Testo = Config()
Testo.initialize()
print(Testo.loginPort,
    Testo.getExchangePort(),
    Testo.getPort(),
    Testo.getDatabaseName())
'''