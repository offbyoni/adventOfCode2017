import unittest
from passphraseChecker import passphraseChecker

class advent4Test(unittest.TestCase):
    def test_CheckInValidphrase(self):
        passphrase = "aa aa bb"
        self.assertFalse(passphraseChecker.checkPhraseValid(passphrase))

if __name__ == '__main__':
    unittest.main()
