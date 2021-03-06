import unittest
import passphraseChecker

class advent4Test(unittest.TestCase):
    def test_checkInValidphrase(self):
        passphrase = "aa bb cc dd aa"
        self.assertFalse(passphraseChecker.checkPhraseValid(passphrase))

    def test_checkValidPassphrase(self):
        passphrase = "aa bb cc dd ee"
        self.assertTrue(passphraseChecker.checkPhraseValid(passphrase))

    def test_checkAnotherValidPassphrase(self):
        passphrase = "aa bb cc dd aaa"
        self.assertTrue(passphraseChecker.checkPhraseValid(passphrase))

    def test_countValidPassphrases(self):
        passphrases = "aa bb cc dd aa\naa bb cc dd ee\naa bb cc dd aaa"
        res = passphraseChecker.countValidPassphrases(passphrases)
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
