from collections.abc import Container
from collections.abc import Sized
import logging

class Graph(Container, Sized):

    def __init__(self):
        self.vertices = []
        self.edges = {}


    def __contains__(self, vert):
        return vert in self.vertices


    def contains_edge(self, edge):
        return edge in self.edges.items()


    def __len__(self):
        return len(self.vertices)


    def parseGraph(self, strings_list):
        for number, line in enumerate(strings_list):
            vert, edges_list = self.__parseSingleLine(line, number)
            if vert is not None and edges_list is not None:
                self.__addEdgesAndVert(vert, edges_list)


    def __parseSingleLine(self, line, number):
        try:
            splited = line.split()
            return splited[0], splited[2:]
        except ValueError:
            logging.warning("Invalid content of graph file in line {}. "
                            "Line skipped".format(number+1))
            return None, None
        except IndexError:
            logging.warning("Empty string of graph file in line {}. "
                            "Line skipped".format(number+1))
            return None, None


    def __addEdgesAndVert(self, vert, edges_list):
        vert, edges_list = self.__convertEdgesAndVertToInt(vert, edges_list)
        self.__addVert(vert)
        self.__addEdge(vert, edges_list)


    def __convertEdgesAndVertToInt(self, vert, edges_list):
        vert = int(vert)
        def f(e):
            if e[-1] is ',':
                return int(e[:-1])
            else:
                return int(e)
        edges_list = [f(e) for e in edges_list]
        return vert, edges_list


    def __addVert(self, vert):
        if vert not in self.vertices:
            self.vertices.append(vert)


    def __addEdge(self, vert, edges_list):
        for edge in edges_list:
            if vert not in self.edges:
                self.edges[vert] = [edge]
            else:
                self.edges[vert].append(edge)


    def empty(self):
        return self.__len__() == 0


    def traverseAll(self, startingNode):
        self.visitedNodes = []
        self.__traverse(startingNode)
        return self.visitedNodes


    def __traverse(self, node):
        self.visitedNodes.append(node)

        for n in self.edges[node]:
            if n not in self.visitedNodes:
                self.__traverse(n)
