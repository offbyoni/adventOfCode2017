def reallocate(banks):
    # highestIndex = findHighestBank(banks)
    # blocks = clearHighestBank(highestIndex, banks)
    # return redistribute(highestIndex, banks, blocks)
    pass

def findHighestBank(banks):
    if len(banks) < 1:
        raise Exception('no banks')
    maxValue = max(banks)
    highestIndex = banks.index(maxValue)
    return highestIndex
