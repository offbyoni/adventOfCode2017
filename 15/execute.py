from generator import *
from judge import *

#genA = generator(40000000, 512, 16807)
#genB = generator(40000000, 191, 48271)
#print(judge(genA, genB))

genA = generatorMod(5000000, 512, 16807, 4)
genB = generatorMod(5000000, 191, 48271, 8)
print(judge(genA, genB))
