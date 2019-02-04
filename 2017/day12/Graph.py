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


    def __addVert(self, vert):
        if vert not in self.vertices:
            self.vertices.append(vert)


    def __addEdge(self, vert, edges_list):
        for edge in edges_list:
            if (vert, edge) not in self.edges.items():
                self.edges[vert] = edge


    def __convertEdgesAndVertToInt(self, vert, edges_list):
        vert = int(vert)
        edges_list = [int(e) for e in edges_list]
        return vert, edges_list


    def __addEdgesAndVert(self, vert, edges_list):
        vert, edges_list = self.__convertEdgesAndVertToInt(vert, edges_list)
        self.__addVert(vert)
        self.__addEdge(vert, edges_list)


    def parseGraph(self, strings_list):
        for number, line in enumerate(strings_list):
            try:
                vert, _, edges_list = line.split()
            except ValueError:
                logging.warning("Invalid content of graph file in line {}. "
                                "Parsing stoped".format(number+1))
                return

            self.__addEdgesAndVert(vert, edges_list)

    def empty(self):
        return self.__len__() == 0
