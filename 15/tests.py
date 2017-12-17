import unittest
from generator import *

class advent15Test(unittest.TestCase):
    def test_generatorA(self):
        genA = generator()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1092455)

    def test_generatorA2(self):
        genA = generator()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1181022009)

    def test_generatorA3(self):
        genA = generator()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 245556042)

    def test_generatorA4(self):
        genA = generator()
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1744312007)

    def test_generatorA5(self):
        genA = generator()
        genA.generate()
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1352636452)

if __name__ == '__main__':
    unittest.main()
