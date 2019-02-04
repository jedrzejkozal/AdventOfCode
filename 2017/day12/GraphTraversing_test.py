import pytest

from GraphTestBase import *

class TestGraphTraversing(GraphTestBase):

    def test_traverse_one_node_graph_all_nodes_are_visited(self, one_node_graph):
        self.parse_graph(one_node_graph)
        startingNode = 0

        visited_nodes = self.sut.traverseAll(startingNode)

        assert set(visited_nodes) == {0}


    def test_traverse_two_nodes_graph_all_nodes_are_visited(self, two_nodes_graph):
        self.parse_graph(two_nodes_graph)
        startingNode = 0

        visited_nodes = self.sut.traverseAll(startingNode)

        assert set(visited_nodes) == {0, 1}


    def test_traverse_two_nodes_graph_with_repteated_edge_all_nodes_are_visited(self, two_nodes_graph_with_repeated_edge):
        self.parse_graph(two_nodes_graph_with_repeated_edge)
        startingNode = 0

        visited_nodes = self.sut.traverseAll(startingNode)

        assert set(visited_nodes) == {0, 1}


    def test_traverse_three_nodes_graph_all_nodes_are_visited(self, three_nodes_graph):
        self.parse_graph(three_nodes_graph)
        startingNode = 0

        visited_nodes = self.sut.traverseAll(startingNode)

        assert set(visited_nodes) == {0, 1, 2}

    def test_traverse_disjointed_graph_all_nodes_are_visited(self, disjointed_graph):
        self.parse_graph(disjointed_graph)
        startingNode = 0

        visitedNodes = self.sut.traverseAll(startingNode)

        assert set(visitedNodes) == {0, 1}
