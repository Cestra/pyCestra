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

from os import system, name
import subprocess as sp

class Console:

    def __init__(self):
        name = 'Cestra - World Server - '
        version = '0.1'
        system('title ' + name + version)

    def clear(self):
        # for windows
        if name == 'nt':
            sp.call('cls',shell=True)

        # for mac and linux (here, os.name is 'posix')
        elif name == 'posix':
            sp.call('clear',shell=True)
