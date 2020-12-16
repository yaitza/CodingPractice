import unittest
from python.sample.l014longestcommonprefix import *


class MyTestCase(unittest.TestCase):
    def test_longestCommonPrefix_1(self):
        self.assertEqual("fl", longestCommonPrefix(["flower", "flow", "flight"]))

    def test_longestCommonPrefix_2(self):
        self.assertEqual("", longestCommonPrefix(["dog","racecar","car"]))

if __name__ == '__main__':
    unittest.main()
