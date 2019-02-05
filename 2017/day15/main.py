from Generator import Generator
from Judge import Judge


generatorA = Generator(722, 16807)
generatorB = Generator(354, 48271)

judge = Judge(generatorA, generatorB)
result1 = judge.calculateCount()
print("1) generators matching pairs count: {}".format(result1))



def multipleOf4Criterion(number):
    return number % 4 == 0
def multipleOf8Criterion(number):
    return number % 8 == 0
generatorA = Generator(722, 16807, criterion=multipleOf4Criterion)
generatorB = Generator(354, 48271, criterion=multipleOf8Criterion)
judgeWithCriterions = Judge(generatorA, generatorB)
result2 = judgeWithCriterions.calculateCount(comparisons=5000000)
print("2) generators matching pairs count: {}".format(result2))
