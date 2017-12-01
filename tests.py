import unittest
from captcha import captcha

class advent1Test(unittest.TestCase):

      def test_1122_3(self):
            input = 1122
            expectedResult = 3
            self.assertEqual(captcha.capt(input), 3);

if __name__ == '__main__':
   unittest.main()
