import unittest
import os

# class gehdahin():
#     def testi(self):
#         path = os.path.abspath("./logon/src/test.py")
#         command = 'python ' + path
#         s = os.system(command)
#         return s

class TestSamples(unittest.TestCase):
    # def test_01(self):
    #     self.assertEqual(gehdahin().testi(), 0)
    def test_02(self):
        self.assertEqual(0 + 1, 1)

if __name__ == '__main__':
    unittest.main()