from Generator import Generator
from Judge import Judge


generatorA = Generator(722, 16807)
generatorB = Generator(354, 48271)

judge = Judge(generatorA, generatorB)
result1 = judge.calculateCount()
print("1) generators matchin count: {}".format(result1))
