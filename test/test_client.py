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

import unittest

from demo_client.client_normal_connection import DemoClient01
from demo_client.client_no_nickname_connection import DemoClient02

class TestClient(unittest.TestCase):

    def test_01_normal_connection(self):
        demoClient = DemoClient01()
        self.result = demoClient.start('unittest-01', 'unittest-01')
        for test_name, result in self.result.items():
            self.assertTrue(result)

    def test_02_no_nickname_connection(self):
        demoClient = DemoClient02()
        self.result = demoClient.start('unittest-02', 'unittest-02')
        for test_name, result in self.result.items():
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
