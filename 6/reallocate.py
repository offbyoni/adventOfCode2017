def reallocate(banks):
    highestIndex = findHighestBank(banks)
    # blocks, banks = clearHighestBank(banks, highestIndex)
    # return redistribute(highestIndex, banks, blocks)
    pass

def findHighestBank(banks):
    if len(banks) < 1:
        raise Exception('no banks')
    maxValue = max(banks)
    highestIndex = banks.index(maxValue)
    return highestIndex

def clearHighestBank(banks, highestIndex):
    if len(banks) < 1:
        raise Exception('no banks')
