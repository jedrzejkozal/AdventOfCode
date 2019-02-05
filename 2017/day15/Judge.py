from Generator import *

class Judge(object):

    def __init__(self, generatorA, generatorB):
        self.generatorA = generatorA
        self.generatorB = generatorB
        self.last16bitsMask = int.from_bytes(b'\xff\xff',
                                byteorder='big', signed=False)


    def calculateCount(self, comparisons=40000000):
        count = 0
        for i in range(comparisons):
            generatedA = next(self.generatorA.generate())
            generatedB = next(self.generatorB.generate())
            if self.__checkForMatch(generatedA, generatedB):
                count += 1
        return count


    def __checkForMatch(self, generatedA, generatedB):
        return self.__getLast16bits(generatedA) == self.__getLast16bits(generatedB)


    def __getLast16bits(self, number):
        return number & self.last16bitsMask
