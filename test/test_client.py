import unittest

from demoClient.client_normal_connection import DemoClient01
from demoClient.client_no_nickname_connection import DemoClient02

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
