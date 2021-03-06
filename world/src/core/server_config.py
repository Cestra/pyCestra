'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

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


class Config:

    def __init__(self):
        # self.log = Logging()
        # self.log.debug('Config instance has been created')
        self.config = configparser.ConfigParser()
        self.world_ip = '127.0.0.1'
        self.world_port = 5555
        self.server_name = 'Jiva'
        self.log_Level = 'DEBUG'
        self.world_db_host = '127.0.0.1'
        self.world_db_port = 3306
        self.world_db_name = 'cestra_world'
        self.world_db_user = 'root'
        self.world_db_passwo = 'root'
        self.exchangeIp = '127.0.0.1'
        self.exchangePort = 451

    def create_default_world_config(self):
        try:
            self.config['WorldServer Basic Settings'] = {
                'world_server_ip': '127.0.0.1',
                'world_server_port': '5555',
                'world_server_name': 'Jiva',
                'world_server_log_level': 'INFO'

            }
            self.config['Database Configuration'] = {
                'world_database_ip': '127.0.0.1',
                'world_database_port': '3306',
                'world_database_name': 'cestra_world',
                'world_database_user': 'root',
                'world_database_pass': 'root'
            }
            self.config['RealmList Configuration'] = {
                'network_realmList_ip': '127.0.0.1',
                'network_realmList_port': '451'
            }
            with open('./world.conf', 'w') as configfile:    # save
                self.config.write(configfile)
            return True
        except:
            return False

    def initialize(self):
        try:
            section01 = 'WorldServer Basic Settings'
            section02 = 'Database Configuration'
            section03 = 'RealmList Configuration'
            self.config.read('./world.conf')

            self.world_ip = self.config.get(section01, 'world_server_ip')
            self.world_port = self.config.getint(section01, 'world_server_port')
            self.server_name = self.config.get(section01, 'world_server_name')
            self.log_Level = self.config.get(section01, 'world_server_log_level')

            self.world_db_host = self.config.get(section02, 'world_database_ip')
            self.world_db_port = self.config.getint(section02, 'world_database_port')
            self.world_db_name = self.config.get(section02, 'world_database_name')
            self.world_db_user = self.config.get(section02, 'world_database_user')
            self.world_db_passwo = self.config.get(section02, 'world_database_pass')

            self.exchangeIp = self.config.get(section03, 'network_realmList_ip')
            self.exchangePort = self.config.getint(section03, 'network_realmList_port')
        except:
            print('Config.initialize: Unreadable config or missing fields')
            # self.log.warning('Config.initialize: Unreadable config or missing fields')

    def get_world_ip(self):
        return self.world_ip

    def get_world_port(self):
        return self.world_port

    def get_server_name(self):
        return self.server_name

    def get_loggin_level(self):
        return self.log_Level

    def get_world_db_host(self):
        return self.world_db_host

    def get_world_db_port(self):
        return self.world_db_port

    def get_world_db_name(self):
        return self.world_db_name

    def get_world_db_user(self):
        return self.world_db_user

    def get_world_db_passwo(self):
        return self.world_db_passwo

    def get_exchange_ip(self):
        return self.exchangeIp

    def get_exchange_port(self):
        return self.exchangePort
