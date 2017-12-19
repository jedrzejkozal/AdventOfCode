

class Trampolines(object):

    def __init__(self):
        self.moves = self.read()
        #self.moves = [0, 3, 0, 1, -3]

    def read(self):
        f = open("input.txt", 'r')
        table = []
        for elem in f:
            table.append(int(elem))

        return table

    def move(self):
        self.moves[self.index] += 1
        self.index += self.moves[self.index]-1

    def modify_move(self):
        if self.moves[self.index] > 3:
            self.moves[self.index] -= 1
        else:
            self.moves[self.index] += 1

    def jump(self):
        self.index = 0
        num_moves = 0
        while self.index > -1 and self.index < len(self.moves):
            self.modify_move()
            if not (self.index > -1 and self.index < len(self.moves)):
                return num_moves
            else:
                self.index += self.moves[self.index]-1
                #print self.index
                #print self.moves[self.index]
                num_moves += 1
        return num_moves

t = Trampolines()
#print t.moves
print t.jump()
