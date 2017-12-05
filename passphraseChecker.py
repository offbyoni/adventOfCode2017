class passphraseChecker():
    def checkPhraseValid(passphrase):
        words = passphrase.split(" ")
        for idx in range(len(words)):
            for idx2 in range (idx+1, len(words)):
                if (words[idx] == words[idx2]):
                    return False
        return True
