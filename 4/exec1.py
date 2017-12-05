import passphraseChecker
with open("input.txt", "r") as myfile:
    data = myfile.read()
    res = passphraseChecker.countValidPassphrases(data)
    print(res)
