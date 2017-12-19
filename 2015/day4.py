import md5

class AdventCoinsDigger:

    def __init__(self):
        self.m = md5.new()

    def digAdveantCoins(self, secretKey):
        pass

    def convertHexToString(self, hex):
        print "hex = %d" % hex
        shex = str(hex)
        for h in shex:
            print str(h),
        print
        return shex

    def checkIfIsALetter(self, c):
        if ord(c) > 96:
            return True
        else:
            return False

    def convertLetterToASCIValue(self, c):
        return ord(c)-87

    def convertNumberToASCIValute(self, n):
        return ord(n)-48

    def convertSingleCharToASCIIValue(self, c):
        if self.checkIfIsALetter(c):
            return self.convertLetterToASCIValue(c)
        else:
            return self.convertNumberToASCIValute(c)

    def convertDoubleCharToASCIValue(self, c):
        return 16*self.convertSingleCharToASCIIValue(c[0])+self.convertSingleCharToASCIIValue(c[1])

    def convertHexToString1(self, shex):
        string = ""
        for i in range(0, len(shex), 2):
            #print shex[i:i+1]
            #print hex(shex[i:i+1])
            print self.convertDoubleCharToASCIValue(shex[i:i+2])
            print chr(self.convertDoubleCharToASCIValue(shex[i:i+2]))
            string += chr(self.convertDoubleCharToASCIValue(shex[i:i+2]))
        print string
        return string

a = AdventCoinsDigger()
#a.m.update('abcdef609043')

i = int(0xabcdef609043)
print "i = %d" % i
#arg = a.convertHexToString(i)
arg = a.convertHexToString1("abcdef609043")
print "arg = %s" % arg
a.m.update(arg)
res = a.m.digest()
print "res = %s" % res
res_i = int(res, 16)
print hex(res_i)
#print hex(res)
