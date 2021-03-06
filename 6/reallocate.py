def reallocationCount(banks):
    previousStates = list()
    count = 0
    while banks not in previousStates:
        previousStates.append(list(banks))
        banks = reallocate(banks)
        count += 1
    return count

def reallocationLoopSize(banks):
    previousStates = list()
    while banks not in previousStates:
        previousStates.append(list(banks))
        banks = reallocate(banks)
    pos = previousStates.index(banks)
    return len(previousStates) - pos

def reallocate(banks):
    highestBankIndex = highestBank(banks)
    banks, blocks = clearHighestBank(banks, highestBankIndex)
    return redistribute(banks, blocks, highestBankIndex)

def highestBank(banks):
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
