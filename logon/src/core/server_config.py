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

import configparser

# Circular import dependency !
# from core.logging_handler import Logging


class Config:

    def __init__(self):
        # self.log = Logging()
        # self.log.debug('Config instance has been created')
        self.config = configparser.ConfigParser()
        self.loginIp = '127.0.0.1'
        self.loginPort = 478
        self.version = '1.29.1'
        self.logLevel = 'DEBUG'
        self.host = '127.0.0.1'
        self.port = 3306
        self.name = 'cestra_logon'
        self.user = 'root'
        self.passwo = 'root'
        self.updateTime = 120
        self.exchangeIp = '127.0.0.1'
        self.exchangePort = 451

    def create_default_logon_config(self):
        try:
            self.config['LogonServer Basic Settings'] = {
                'logon_server_ip': '127.0.0.1',
                'logon_server_port': '478',
                'logon_server_version': '1.29.1',
                'logon_server_log_level': 'INFO'

            }
            self.config['Database Configuration'] = {
                'logon_database_ip': '127.0.0.1',
                'logon_database_port': '3306',
                'logon_database_name': 'cestra_game',
                'logon_database_user': 'root',
                'logon_database_pass': 'fabio312',
                'logon_database_update_service': '120'
            }
            self.config['RealmList Configuration'] = {
                'network_realmList_ip': '127.0.0.1',
                'network_realmList_port': '451'
            }
            with open('./logon.conf', 'w', encoding='utf-8') as configfile:    # save
                self.config.write(configfile)
            return True
        except:
            return False

    def initialize(self):
        try:
            section01 = 'LogonServer Basic Settings'
            section02 = 'Database Configuration'
            section03 = 'RealmList Configuration'
            self.config.read('./logon.conf')

            self.loginIp = self.config.get(section01, 'logon_server_ip')
            self.loginPort = self.config.getint(section01, 'logon_server_port')
            self.version = self.config.get(section01, 'logon_server_version')
            self.logLevel = self.config.get(section01, 'logon_server_log_level')

            self.host = self.config.get(section02, 'logon_database_ip')
            self.port = self.config.getint(section02, 'logon_database_port')
            self.name = self.config.get(section02, 'logon_database_name')
            self.user = self.config.get(section02, 'logon_database_user')
            self.passwo = self.config.get(section02, 'logon_database_pass')
            self.updateTime = self.config.getint(section02, 'logon_database_update_service')

            self.exchangeIp = self.config.get(section03, 'network_realmList_ip')
            self.exchangePort = self.config.getint(section03, 'network_realmList_port')
        except:
            print('Config.initialize: Unreadable config or missing fields')
            # self.log.warning('Config.initialize: Unreadable config or missing fields')

    def get_login_ip(self):
        return self.loginIp

    def get_login_port(self):
        return self.loginPort

    def get_version(self):
        return self.version
    
    def get_loggin_level(self):
        return self.logLevel

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
    
    def get_update_time(self):
        return self.updateTime

    def get_exchange_ip(self):
        return self.exchangeIp

    def get_exchange_port(self):
        return self.exchangePort
