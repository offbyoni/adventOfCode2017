import unittest
from reallocate import *

class advent6Test(unittest.TestCase):
    def test_findHighestBank(self):
        banks = [0, 2, 7, 0]
        highestIndex = findHighestBank(banks)
        self.assertEqual(highestIndex, 2)

    def test_findHighestBankEmpty(self):
        banks = []
        with self.assertRaises(Exception) as context:
            findHighestBank(banks)
        self.assertTrue('no banks' in str(context.exception))

    def test_findHighestBank3(self):
        banks = [100, 20, 50, 0, 9, 600, 1000]
        highestIndex = findHighestBank(banks)
        self.assertEqual(highestIndex, 6)

    def test_findHighestBankTwoEqual(self):
        banks = [1, 2, 3, 5, 5]
        highestIndex = findHighestBank(banks)
        self.assertEqual(highestIndex, 3)

    def test_clearHighestBankEmpty(self):
        banks = []
        with self.assertRaises(Exception) as context:
            clearHighestBank(banks, 0)
        self.assertTrue('no banks' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
