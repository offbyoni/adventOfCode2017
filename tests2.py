import unittest
from myChecksum2 import myChecksum2

class advent2Test(unittest.TestCase):

    def test_onlyTest(self):
        inputs = "5 9 2 8\n9 4 7 3\n3 8 6 5"
        expectedResult = 9
        res = myChecksum2.check(inputs)
        self.assertEqual(res, expectedResult)

if __name__ == '__main__':
    unittest.main()
