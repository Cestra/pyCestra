import unittest

from client_normal_customer_connection import DemoClient

class TestClient(unittest.TestCase):

    def test_01_connection(self):
        demoClient = DemoClient()
        self.result = demoClient.start('admin', 'admin')
        self.assertEqual(self.result['test_connection'], True)
        self.assertEqual(self.result["test_key_response"], 1)

if __name__ == '__main__':
    unittest.main()
