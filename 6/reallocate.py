def reallocate(banks):
    highestBankIndex = findHighestBank(banks)
    blocks, banks = clearHighestBank(banks, highestBankIndex)
    # return redistribute(banks, blocks, highestBankIndex)
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
    blocks = banks[highestBankIndex]
    banks[highestBankIndex] = 0
    return banks, blocks

def redistribute(banks, blocks, highestBankIndex):
    for i in range (0, blocks):
        highestBankIndex = (highestBankIndex + 1) % len(banks)
        banks[highestBankIndex] += 1
    return banks
