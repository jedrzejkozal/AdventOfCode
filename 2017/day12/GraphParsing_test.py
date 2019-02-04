import pytest

from Graph import *

class TestGraphParsing(object):

    """
    0 -
    ↑__|

    """
    @pytest.fixture(scope="class")
    def one_node_graph(self):
        return ["0 <-> 0"]


    """
    ↙ --- \
    0 --→ 1
    """
    @pytest.fixture(scope="class")
    def two_node_graph(self):
        return [      "1"
                 " <-> "
                "0",
                "0 <-> 1",
                ]


    """
    ↙ --- \
    ↙ --- \
    0 --→ 1
    """
    @pytest.fixture(scope="class")
    def two_node_graph_with_repeated_edge(self):
        return [      "1"
                 " <-> "
                "0",
                      "1"
                 " <-> "
                "0",
                "0 <-> 1"]


    """
    ↙ --- \
    0 --→ 1
     ↖ \
      \ \
       \ ↘
          2
    """
    @pytest.fixture(scope="class")
    def three_node_graph(self):
        return [      "1"
                 " <-> "
                "0",
                "0 <-> 1",
                "0"
                 " <-> "
                      "2",
                      "2"
                 " <-> "
                "0"]


    @classmethod
    def setup(cls):
        cls.sut = Graph()


    def test_parse_graph_with_no_node_graph_is_empty(self):
        arg = [""]
        self.sut.parseGraph(arg)
        assert self.sut.empty() == True


    def test_parse_graph_with_one_node_graph_is_not_empty(self):
        arg = self.one_node_graph()
        self.sut.parseGraph(arg)
        assert self.sut.empty() == False


    def test_parse_graph_with_one_node_graph_contains_vertcies(self):
        arg = self.one_node_graph()
        self.sut.parseGraph(arg)
        assert 0 in self.sut


    def test_parse_graph_with_one_node_graph_contains_edges(self):
        arg = self.one_node_graph()
        self.sut.parseGraph(arg)

        #vert 0:
        assert self.sut.contains_edge((0, [0]))


    def test_parse_graph_with_two_nodes_graph_is_not_empty(self):
        arg = self.two_node_graph()

        self.sut.parseGraph(arg)
        assert self.sut.empty() == False


    def test_parse_graph_with_two_nodes_graph_contains_verticies(self):
        arg = self.two_node_graph()

        self.sut.parseGraph(arg)
        assert 0 in self.sut
        assert 1 in self.sut


    def test_parse_graph_with_two_nodes_graph_contains_edges(self):
        arg = self.two_node_graph()

        self.sut.parseGraph(arg)
        #vert 0:
        assert self.sut.contains_edge((0, [1]))
        #vert 1:
        assert self.sut.contains_edge((1, [0]))


    def test_parse_graph_with_two_nodes_and_uneacesseary_connections_edges_are_added_once(self):
        arg = self.two_node_graph_with_repeated_edge()

        self.sut.parseGraph(arg)
        #vert 0:
        assert self.sut.contains_edge((0, [1]))
        #vert 1:
        assert self.sut.contains_edge((1, [0, 0]))


    def test_parse_graph_with_three_nodes_graph_is_not_empty(self):
        arg = self.three_node_graph()

        self.sut.parseGraph(arg)
        assert self.sut.empty() == False


    def test_parse_graph_with_three_nodes_graph_contains_verticies(self):
        arg = self.three_node_graph()

        self.sut.parseGraph(arg)
        #vert 0:
        assert 0 in self.sut
        assert 1 in self.sut
        assert 2 in self.sut


    def test_parse_graph_with_three_nodes_graph_contains_edges(self):
        arg = self.three_node_graph()

        self.sut.parseGraph(arg)
        #vert 0:
        assert self.sut.contains_edge((0, [1, 2]))
        assert self.sut.contains_edge((1, [0]))
        assert self.sut.contains_edge((2, [0]))
