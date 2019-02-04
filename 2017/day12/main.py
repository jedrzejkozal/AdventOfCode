

def readGraph(filename):
    f = open(filename, 'r')
    result = f.readlines()
    f.close()
    return result


readGraph("input1.txt")
