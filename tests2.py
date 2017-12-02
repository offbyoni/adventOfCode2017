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

if __name__ == '__main__':
   unittest.main()
