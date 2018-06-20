from math import sqrt
from math import floor
from math import ceil
from math import fabs

class UlamSprial:

    def getPositionOfBegining(self, value):
        x = floor(sqrt(value)/2)
        return x, -x

    def getValueOfBeginingForSomeNumber(self, numb):
        s = sqrt(numb)
        if floor(s) % 2 == 0:
            return (floor(s) + 1) ** 2
        else:
            return (floor(s) + 2) ** 2

    def getLengthOffSqaureForBegining(self, begin):
        return sqrt(begin)

    def getCornersForBegin(self, begin):
        side_len = self.getLengthOffSqaureForBegining(begin)-1
        return (begin, begin - side_len, begin - 2*side_len, begin - 3*side_len)

    def getNerestCorner(self, number, corners):
        diff = float('inf')
        corner = 0
        for c in corners:
            if fabs(c - number) < diff:
                diff = fabs(c - number)
                corner = c
        print "nearest corner = %d" % corner
        return corner

    def findNearestCorner(self, number, begin):
        corners = self.getCornersForBegin(begin)
        return self.getNerestCorner(number, corners)

    def getPositionOfNumber(self, number):
        begin = self.getValueOfBeginingForSomeNumber(number)
        print "begin = %d" % begin
        bx, by = self.getPositionOfBegining(begin)
        print "bx, by = %d, %d" % (bx, by)

        corner = self.findNearestCorner(number, begin)

        print "fabs = %d" % fabs(corner - number)
        print "returning = %d" % (bx - by - fabs(corner - number))
        return bx - by - fabs(corner - number)


class FibonaciUlamSprial:

    def __init__(self):
        self.dictionary = {(0,0):1,(1,0):1}
        self.neighbours = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        self.previos_move = (0,1)

    def getNeighboursPositions(self, point_pos):
        neighbours_pos = []
        for n in self.neighbours:
            try:
                f = self.dictionary[(point_pos[0]+n[0], point_pos[1]+n[1])]
            except KeyError, e:
                continue
            neighbours_pos.append((point_pos[0]+n[0], point_pos[1]+n[1]))
        return neighbours_pos

    def getValueOfNextPosition(self, postion):
        neighbours = self.getNeighboursPositions(postion)
        #print neighbours
        sum = 0
        for n in neighbours:
            sum += self.dictionary[n]
        return sum

    def detectCorner(self, pos):
        if pos[0]-1 > 0 and pos[1] < 0 and pos[0]-1 == -pos[1]:
            self.previos_move = (0,1)
            return pos[0], pos[1]+1
        elif pos[0] > 0 and pos[1] > 0 and pos[0] == pos[1]:
            self.previos_move = (-1,0)
            return pos[0]-1, pos[1]
        elif pos[0] < 0 and pos[1] > 0 and pos[0] == -pos[1]:
            self.previos_move = (0,-1)
            return pos[0], pos[1]-1
        elif pos[0] < 0 and pos[1] < 0 and pos[0] == pos[1]:
            self.previos_move = (1,0)
            return pos[0]+1, pos[1]
        return None

    def getNextPosition(self, pos):
        detected = self.detectCorner(pos)
        if detected != None:
            return detected
        else:
            return pos[0]+self.previos_move[0], pos[1]+self.previos_move[1]

    def getFistThatIsLager(self, threshold):
        pos = (1,0)
        val = 0
        while val < threshold:
            pos = self.getNextPosition(pos)
            val = self.getValueOfNextPosition(pos)
            self.dictionary[pos] = val

        return val



if __name__ == '__main__':
    #u = UlamSprial()
    #print u.getPositionOfNumber(325489)

    f = FibonaciUlamSprial()
    print f.getFistThatIsLager(325489)

    #print f.dictionary
