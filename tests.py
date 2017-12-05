import unittest
from passphraseChecker import passphraseChecker

class advent4Test(unittest.TestCase):
    def test_checkInValidphrase(self):
        passphrase = "aa bb cc dd aa"
        self.assertFalse(passphraseChecker.checkPhraseValid(passphrase))

    def test_checkValidPassphrase(self):
        passphrase = "aa bb cc dd ee"
        self.assertTrue(passphraseChecker.checkPhraseValid(passphrase))

if __name__ == '__main__':
    unittest.main()
