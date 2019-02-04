import pytest

"""
0 -
↑__|

"""
@pytest.fixture
def one_node_graph():
    return ["0 <-> 0"]


"""
↙ --- \
0 --→ 1
"""
@pytest.fixture
def two_nodes_graph():
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
@pytest.fixture
def two_nodes_graph_with_repeated_edge():
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
@pytest.fixture
def three_nodes_graph():
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


"""
↙ --- \
0 --→ 1

↙ --- \
2 --→ 3
"""
@pytest.fixture
def disjointed_graph():
    return [      "1"
             " <-> "
            "0",
            "0 <-> 1",
                  "3"
             " <-> "
            "2",
            "2 <-> 3",
            ]
