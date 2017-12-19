

class MemoryBanks(object):

    def __init__(self):
        self.banks = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
        #self.banks = [0, 2, 7, 0]

    def find_max(self, list):
        _max = -9999
        _i = 0
        for i in range(len(list)):
            if _max < list[i]:
                _i = i
                _max = list[i]

        return _i, _max

    def move(self, b):
        #print self.banks
        i, cash = self.find_max(b)
        part = cash / len(b)
        rest = cash % len(b)
        #print part
        b[i] = 0
        #print self.banks
        b_new = [x + part for x in b]
        b[i] = cash
        #print self.banks
        numb_of_moves = rest
        i += 1
        while numb_of_moves > 0:
            if i == len(b_new):
                i = 0
            b_new[i] += 1
            numb_of_moves -= 1
            i += 1
        #self.banks = b
        return b_new
        #print self.banks

    def condtion(self, b_list):
        if b_list not in self.history:
            return True
        else:
            return False

    def equlize(self):
        self.history = []
        i = 0
        b = self.banks

        #for i in range(5):
        while self.condtion(b):
            self.history.append(b)
            #print self.banks
            #print self.history
            b = self.move(b)
            i += 1
        self.banks = b
        return i

mb = MemoryBanks()
#mb.move()
i = mb.equlize()
print i
print mb.history.index(mb.banks) - i
print
