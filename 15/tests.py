import unittest
from generator import *
from judge import *

class advent15Test(unittest.TestCase):
    def test_generatorA(self):
        genA = generator(5, 65, 16807)
        self.assertEqual(list(genA), [1092455, \
                                1181022009, \
                                245556042, \
                                1744312007, \
                                1352636452])

    def test_generatorB(self):
        genB = generator(5, 8921, 48271)
        self.assertEqual(list(genB), [430625591, \
                                1233683848, \
                                1431495498, \
                                137874439, \
                                285222916])

    def test_judge(self):
        genA = generator(5, 65, 16807)
        genB = generator(5, 8921, 48271)
        self.assertEqual(judge(genA, genB), 1)

    def test_generatorModA(self):
        genA2 = generatorMod(5, 65, 16807, 4)
        self.assertEqual(list(genA2), [1352636452, \
                                1992081072, \
                                530830436, \
                                1980017072, \
                                740335192])

    def test_generatorModB(self):
        genB2 = generatorMod(5, 8921, 48271, 8)
        self.assertEqual(list(genB2), [1233683848, \
                                862516352, \
                                1159784568, \
                                1616057672, \
                                412269392])

if __name__ == '__main__':
    unittest.main()
