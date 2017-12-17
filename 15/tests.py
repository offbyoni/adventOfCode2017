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
        genB = generator(5, 8921, 48271)
        genA = generator(5, 65, 16807)
        self.assertEqual(judge(genA, genB), 1)

if __name__ == '__main__':
    unittest.main()
