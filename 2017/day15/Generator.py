class Generator(object):

    def __init__(self, startingValue, generatorConst):
        self.actualValue = startingValue
        self.generatorConst = generatorConst


    def generateNextValue(self):
        self.actualValue = (self.actualValue * self.generatorConst) % 2147483647


    def generate(self):
        while True:
            self.generateNextValue()
            yield self.actualValue
