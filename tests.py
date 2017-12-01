import unittest
from captcha import captcha

class advent1Test(unittest.TestCase):

      def test_1122_3(self):
            input = 1122
            expectedResult = 3
            self.assertEqual(captcha.capt(input), 3);

      def test_1111_4(self):
            input = 1111
            expectedResult = 4
            self.assertEqual(captcha.capt(input), 4)

if __name__ == '__main__':
   unittest.main()
