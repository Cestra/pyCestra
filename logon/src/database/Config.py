import configparser

class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        try:
            section01 = 'LogonServer Database'
            # TODO Der Pfard wir in der CMD von Windoof nicht gefunden!
            self.config.read('./logon.conf')
            ip = self.config.get(section01, 'logon_database_ip')
            port = self.config.getint(section01, 'logon_database_port')
            name = self.config.get(section01, 'logon_database_name')
            user = self.config.get(section01, 'logon_database_user')
            passwo = self.config.get(section01, 'logon_database_pass')
            # self.__datalist = [ip, port, user, passwo, name]
            self.__datadict = {"ip":ip, "port":port, "name":name, "user":user, "pass":passwo}
        except:
            print("Die logon.conf konnte NICHT erfolgreich ausgelesen werden")
    
    def get(self):
        return self.__datadict

    def createDefault(self):
        try:
            self.config["LogonServer Database"] = {
            'logon_database_ip': '127.0.0.1',
            'logon_database_port': '3306',
            'logon_database_name': 'cestra_game',
            'logon_database_user': 'root',
            'logon_database_pass': 'fabio312'
            }
            with open('./logon.conf', 'w') as configfile:    # save
                self.config.write(configfile)
            return True
        except:
            return False

# Config().createDefault()
# DbConfig = Config()
# print(type(DbConfig.get()))
# print(DbConfig.get())
# data = DbConfig.get()
# print(data['ip'])