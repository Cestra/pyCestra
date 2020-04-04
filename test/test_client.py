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

import unittest

from demo_client.client_normal_connection import DemoClient01
from demo_client.client_no_nickname_connection import DemoClient02

class TestClient(unittest.TestCase):

    def test_01_normal_connection(self):
        demoClient = DemoClient01()
        self.result = demoClient.start('unittest-01', 'unittest-01')
        self.assertEqual(self.result['test_connection'], True)
        self.assertEqual(self.result['test_key_response'], True)
        self.assertEqual(self.result['test_packet_01'], True)
        self.assertEqual(self.result['test_packet_02'], True)
        self.assertEqual(self.result['test_packet_03'], True)
        self.assertEqual(self.result['test_packet_04'], True)
        self.assertEqual(self.result['test_packet_05'], True)
        self.assertEqual(self.result['test_packet_06'], True)
        self.assertEqual(self.result['test_packet_07'], True)

    def test_02_no_nickname_connection(self):
        demoClient = DemoClient02()
        self.result = demoClient.start('unittest-02', 'unittest-02')
        self.assertEqual(self.result['test_connection'], True)
        self.assertEqual(self.result['test_key_response'], True)
        self.assertEqual(self.result['test_packet_00'], True)
        self.assertEqual(self.result['test_packet_01'], True)
        self.assertEqual(self.result['test_packet_02'], True)
        self.assertEqual(self.result['test_packet_03'], True)
        self.assertEqual(self.result['test_packet_04'], True)
        self.assertEqual(self.result['test_packet_05'], True)
        self.assertEqual(self.result['test_packet_06'], True)
        self.assertEqual(self.result['test_packet_07'], True)

if __name__ == '__main__':
    unittest.main()
