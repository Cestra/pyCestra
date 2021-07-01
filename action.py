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

import os
import threading
from typing_extensions import runtime

runtime = 30
name = ["logon-Server","world-Server","server-unittest"]

def lthread():
    try:
        t = threading.Thread(target=logonServer,name=name[0],args=runtime)
        t.start()
    except threading.ThreadError as e:
        print('Login Server could not be created: ' + str(e))

def logonServer():
    os.system('python logon/src/main.py')
    pass


testthread()