def reallocate(banks):
    highestBankIndex = findHighestBank(banks)
    # blocks, banks = clearHighestBank(banks, highestBankIndex)
    # return redistribute(highestBankIndex, banks, blocks)
    pass

def findHighestBank(banks):
    if len(banks) < 1:
        raise Exception('no banks')
    maxValue = max(banks)
    highestBankIndex = banks.index(maxValue)
    return highestBankIndex

def clearHighestBank(banks, highestBankIndex):
    if len(banks) < 1:
        raise Exception('no banks')
    if highestBankIndex > len(banks) - 1 or highestBankIndex < 0:
        raise Exception('index out of bounds')
    return [1, 0, 2, 6], 30
