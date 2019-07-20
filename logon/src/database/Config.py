import configparser

class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.default_config = {'ip':'127.0.0.1',
                            'port':3306,
                            'name':'cestra_game',
                            'user':'root',
                            'pass':'fabio312'}
        try:
            section01 = 'LogonServer Database'
            # TODO The path is not found in the CMD of Windows!
            self.config.read('./logon.conf')
            ip = self.config.get(section01, 'logon_database_ip')
            port = self.config.getint(section01, 'logon_database_port')
            name = self.config.get(section01, 'logon_database_name')
            user = self.config.get(section01, 'logon_database_user')
            passwo = self.config.get(section01, 'logon_database_pass')
            self.__datadict = {'ip':ip, 'port':port, 'name':name, 'user':user, 'pass':passwo}
        except:
            print('[WARNING] The logon.conf CAN´T be successfully read\nThe default config is used')
            self.__datadict = self.default_config
    
    def get(self):
        return self.__datadict

    def createDefault(self):
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

# ======================================================================

    # self.config = configparser.ConfigParser()

    def initialize(self):
        try:
            section01 = 'LogonServer Database'
            section02 = 'Network RealmList'
            section03 = 'Logon Server'
            config.read('./logon.conf')

            self.ip = self.config.get(section01, 'logon_database_ip')
            self.port = self.config.getint(section01, 'logon_database_port')
            self.name = self.config.get(section01, 'logon_database_name')
            self.user = self.config.get(section01, 'logon_database_user')
            self.passwo = self.config.get(section01, 'logon_database_pass')

            self.exchangeIp = self.config.get(section02, 'Network_RealmList_Ip')
            self.exchangePort = self.config.get(section02, 'Network_RealmList_Port')

            self.loginIp = (section03, 'Logon_Server_Ip')
            self.loginPort = (section03, 'Logon_Server_Port')
            self.version = (section03, 'Logon_Server_Version')
        except:
            print('[ERROR] Config.initialize: Unreadable config or missing fields')
    




Config().createDefault()
# DbConfig = Config()
# print(type(DbConfig.get()))
# print(DbConfig.get())
# data = DbConfig.get()
# print(data['ip'])