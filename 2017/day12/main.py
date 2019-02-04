from Graph import *

def readGraph(filename):
    f = open(filename, 'r')
    result = f.readlines()
    f.close()
    return result


graph_string = readGraph("input1.txt")
graph = Graph()
graph.parseGraph(graph_string)
result = graph.traverseAll(0)

print("Number of traversed elements : {}".format(len(result)))

numberOfGroups = graph.countGroups()
print("Number of groups: {}".format(numberOfGroups))
