import pytest

from GraphTestBase import *


class TestGraphGroupCounting(GraphTestBase):

    def test_countGroups_for_one_node_graph_returns_1(self, one_node_graph):
        self.parse_graph(one_node_graph)

        assert self.sut.countGroups() == 1

    def test_countGroups_for_disjointed_graph_return_2(self, disjointed_graph):
        self.parse_graph(disjointed_graph)

        assert self.sut.countGroups() == 2
