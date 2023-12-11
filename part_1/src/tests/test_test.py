import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from testclass import TestClass


class TestTest(unittest.TestCase):
    def test_test(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
