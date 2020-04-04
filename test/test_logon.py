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

# import unittest
# import os
# import threading
# import time
# import sys


# class LogonServerDemo(object):

#     def __init__(self):
#         print('DEMO START')

#     def server(self):
#         t = threading.currentThread()
#         while getattr(t, "do_run", True):
#             try:
#                 path = os.path.abspath("./logon/src/main.py")
#                 command = 'python ' + path
#                 os.system(command)
#             except:
#                 print('LOGON MAIN.py kann nicht gestart werden')
#         print("Stopping as you wish.")

#     def start(self):
#         threadName = 'DEMO-SERVER'
#         t = threading.Thread(target=LogonServerDemo.server,
#                             name=threadName,
#                             args=(self,))
#         t.start()
#         print
    
#     def stop(self):
#         sys.exit(0)

# class TestSamples(unittest.TestCase):
#     def test_01(self):
#         demo = LogonServerDemo()
#         x = demo.start()
#         time.sleep(10)
#         demo.stop()
#         self.assertEqual(x, 'ding')

# if __name__ == '__main__':
#     unittest.main()