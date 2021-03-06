import unittest
from captcha2 import captcha2

class advent1Test2(unittest.TestCase):
      def test_1212_6(self):
            input = "1212"
            res = captcha2.capt2(input)
            self.assertEqual(res, 6)

      def test_1221_0(self):
            input = "1221"
            res = captcha2.capt2(input)
            self.assertEqual(res, 0)

      def test_123425_4(self):
            input = "123425"
            res = captcha2.capt2(input)
            self.assertEqual(res, 4)

      def test_123123_12(self):
            input = "123123"
            res = captcha2.capt2(input)
            self.assertEqual(res, 12)

      def test_12131415_4(self):
            input = "12131415"
            res = captcha2.capt2(input)
            self.assertEqual(res, 4)

if __name__ == '__main__':
   unittest.main()
