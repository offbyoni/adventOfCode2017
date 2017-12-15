import unittest
from reallocate import *

class advent6Test(unittest.TestCase):
    def test_findHighestBank(self):
        banks = [0, 2, 7, 0]
        highestBankIndex = findHighestBank(banks)
        self.assertEqual(highestBankIndex, 2)

    def test_findHighestBankEmpty(self):
        banks = []
        with self.assertRaises(Exception) as context:
            findHighestBank(banks)
        self.assertTrue('no banks' in str(context.exception))

    def test_findHighestBank3(self):
        banks = [100, 20, 50, 0, 9, 600, 1000]
        highestBankIndex = findHighestBank(banks)
        self.assertEqual(highestBankIndex, 6)

    def test_findHighestBankTwoEqual(self):
        banks = [1, 2, 3, 5, 5]
        highestBankIndex = findHighestBank(banks)
        self.assertEqual(highestBankIndex, 3)

    def test_clearHighestBankEmpty(self):
        banks = []
        with self.assertRaises(Exception) as context:
            clearHighestBank(banks, 0)
        self.assertTrue('no banks' in str(context.exception))

    def test_clearHighestBankHighIndex(self):
        banks = [0, 2, 3, 4]
        highestBankIndex = 5
        with self.assertRaises(Exception) as context:
            clearHighestBank(banks, highestBankIndex)
        self.assertTrue('index out of bounds' in str(context.exception))

    def test_clearHighestBankNegativeIndex(self):
        banks = [0, 2, 3, 4]
        highestBankIndex = -5
        with self.assertRaises(Exception) as context:
            clearHighestBank(banks, highestBankIndex)
        self.assertTrue('index out of bounds' in str(context.exception))

    def test_clearHighestBank(self):
        banks = [1, 30, 2, 6]
        highestBankIndex = 1
        banks, blocks = clearHighestBank(banks, highestBankIndex)
        self.assertEqual(banks, [1, 0, 2, 6])
        self.assertEqual(blocks, 30)

    def test_redistribute(self):
        banks = [1, 0, 2, 6]
        blocks = 5
        index = 1
        banks = redistribute(banks, blocks, index)
        expectedBanks = [2, 1, 4, 7]
        self.assertEqual(banks, expectedBanks)

if __name__ == '__main__':
    unittest.main()
