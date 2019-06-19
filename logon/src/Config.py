import configparser

class Config():

    def __init__(self):
        self.config = configparser.ConfigParser()

    def createDefault(self):
        try:
            self.config["LogonServer Database"] = {
            'logon_database_ip': '127.0.0.1',
            'logon_database_port': '3306',
            'logon_database_name': 'cestra_game',
            'logon_database_user': 'root',
            'logon_database_pass': 'fabio312'
            }
            with open('./Non/logon.conf', 'w') as configfile:    # save
                self.config.write(configfile)
            return True
        except:
            return False
    
    def getDatafromLogonServerDatabase(self):
        try:
            section01 = 'LogonServer Database'
            self.config.read('./Non/logon.conf')
            ip = self.config.get(section01, 'logon_database_ip')
            port = self.config.getint(section01, 'logon_database_port')
            name = self.config.get(section01, 'logon_database_name')
            user = self.config.get(section01, 'logon_database_user')
            passwo = self.config.get(section01, 'logon_database_pass')
            datalist = [ip, port, user, passwo, name]
            return datalist
        except:
            # print("Die logon.conf konnte NICHT erfolgreich ausgelesen werden")
            return False

# Config().createDefault()
# DbConfig = Config().getDatafromLogonServerDatabase()
# print(DbConfig)
# print(type(DbConfig['port']))