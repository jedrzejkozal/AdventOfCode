import pytest

from Graph import *

class GraphTestBase(object):

    @pytest.fixture(scope="class")
    def parse_graph(self, nodes):
        self.sut.parseGraph(nodes)

    @classmethod
    def setup(cls):
        cls.sut = Graph()
