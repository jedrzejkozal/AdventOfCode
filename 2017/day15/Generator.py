class Generator(object):

    def __init__(self, startingValue, generatorConst, criterion=None):
        self.actualValue = startingValue
        self.generatorConst = generatorConst
        self.performCriterionTest = criterion


    def generateNextValue(self):
        self.actualValue = (self.actualValue * self.generatorConst) % 2147483647


    def generate(self):
        while True:
            self.generateNextValue()
            if self.performCriterionTest is not None:
                while self.performCriterionTest(self.actualValue) == False:
                    self.generateNextValue()
            yield self.actualValue
