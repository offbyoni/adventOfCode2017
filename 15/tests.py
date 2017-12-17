import unittest
from generator import *

class advent15Test(unittest.TestCase):
    def test_generatorA(self):
        genA = generator(65, 16807)
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1092455)

    def test_generatorA2(self):
        genA = generator(65, 16807)
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1181022009)

    def test_generatorA3(self):
        genA = generator(65, 16807)
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 245556042)

    def test_generatorA4(self):
        genA = generator(65, 16807)
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1744312007)

    def test_generatorA5(self):
        genA = generator(65, 16807)
        genA.generate()
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1352636452)

    def test_generatorB(self):
        genA = generator(8921, 48271)
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 430625591)

    def test_generatorB2(self):
        genA = generator(8921, 48271)
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1233683848)

    def test_generatorB3(self):
        genA = generator(8921, 48271)
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 1431495498)

    def test_generatorB4(self):
        genA = generator(8921, 48271)
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 137874439)

    def test_generatorB5(self):
        genA = generator(8921, 48271)
        genA.generate()
        genA.generate()
        genA.generate()
        genA.generate()
        firstNumber = genA.generate()
        self.assertEqual(firstNumber, 285222916)

if __name__ == '__main__':
    unittest.main()
