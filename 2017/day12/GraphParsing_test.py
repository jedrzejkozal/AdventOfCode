import pytest

from Graph import *

class TestGraphParsing(object):

    @classmethod
    def setup(cls):
        cls.sut = Graph()


    def test_parse_graph_with_no_node_graph_is_empty(self):
        arg = [""]
        self.sut.parseGraph(arg)
        assert self.sut.empty() == True


    def test_parse_graph_with_one_node_graph_is_not_empty(self, one_node_graph):
        self.sut.parseGraph(one_node_graph)
        assert self.sut.empty() == False


    def test_parse_graph_with_one_node_graph_contains_vertcies(self, one_node_graph):
        self.sut.parseGraph(one_node_graph)
        assert 0 in self.sut


    def test_parse_graph_with_one_node_graph_contains_edges(self, one_node_graph):
        self.sut.parseGraph(one_node_graph)

        #vert 0:
        assert self.sut.contains_edge((0, [0]))


    def test_parse_graph_with_two_nodes_graph_is_not_empty(self, two_nodes_graph):
        self.sut.parseGraph(two_nodes_graph)
        assert self.sut.empty() == False


    def test_parse_graph_with_two_nodes_graph_contains_verticies(self, two_nodes_graph):
        self.sut.parseGraph(two_nodes_graph)
        assert 0 in self.sut
        assert 1 in self.sut


    def test_parse_graph_with_two_nodes_graph_contains_edges(self, two_nodes_graph):
        self.sut.parseGraph(two_nodes_graph)
        #vert 0:
        assert self.sut.contains_edge((0, [1]))
        #vert 1:
        assert self.sut.contains_edge((1, [0]))


    def test_parse_graph_with_two_nodes_and_uneacesseary_connections_edges_are_added_once(self, two_nodes_graph_with_repeated_edge):
        self.sut.parseGraph(two_nodes_graph_with_repeated_edge)
        #vert 0:
        assert self.sut.contains_edge((0, [1]))
        #vert 1:
        assert self.sut.contains_edge((1, [0, 0]))


    def test_parse_graph_with_three_nodes_graph_is_not_empty(self, three_nodes_graph):
        self.sut.parseGraph(three_nodes_graph)
        assert self.sut.empty() == False


    def test_parse_graph_with_three_nodes_graph_contains_verticies(self, three_nodes_graph):
        self.sut.parseGraph(three_nodes_graph)
        #vert 0:
        assert 0 in self.sut
        assert 1 in self.sut
        assert 2 in self.sut


    def test_parse_graph_with_three_nodes_graph_contains_edges(self, three_nodes_graph):
        self.sut.parseGraph(three_nodes_graph)
        #vert 0:
        assert self.sut.contains_edge((0, [1, 2]))
        assert self.sut.contains_edge((1, [0]))
        assert self.sut.contains_edge((2, [0]))
