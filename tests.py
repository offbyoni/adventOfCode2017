import unittest
from captcha import captcha

class advent1Test(unittest.TestCase):

      def test_1122_3(self):
            input = "1122"
            expectedResult = 3
            self.assertEqual(captcha.capt(input), 3);

      def test_1111_4(self):
            input = "1111"
            expectedResult = 4
            self.assertEqual(captcha.capt(input), 4)

      def test_1234_0(self):
            input = "1234"
            expectedResult = 0
            self.assertEqual(captcha.capt(input), 0)

      def test_91212129_9(self):
            input = "91212129"
            expectedResult = 9
            self.assertEqual(captcha.capt(input), 9)

if __name__ == '__main__':
   unittest.main()
