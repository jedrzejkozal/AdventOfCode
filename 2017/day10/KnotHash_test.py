import pytest

from KnotHash import *

@pytest.mark.incremental
class TestKnotHash(object):

    @classmethod
    def setup(cls):
        cls.list = [0, 1, 2, 3, 4]
        cls.input_length = [3, 4, 1, 5]

        cls.sut = KnotHash(cls.list, cls.input_length)

    def test_input_length_3(self):
        self.sut.knot(3)
        assert(self.sut.list == [2, 1, 0, 3, 4])

    def test_input_length_4(self):
        self.test_input_length_3()
        self.sut.knot(4)
        assert(self.sut.list == [4, 3, 0, 1, 2]) #[2, 1, 0, 3, 4]

    def test_input_length_1(self):
        self.test_input_length_4()
        self.sut.knot(1)
        assert(self.sut.list == [4, 3, 0, 1, 2]) #[4, 3, 0, 1, 2]

    def test_input_length_5(self):
        self.test_input_length_1()
        self.sut.knot(5)
        assert(self.sut.list == [3, 4, 2, 1, 0]) #[4, 3, 0, 1, 2]

    """
    def test_whole(self):
        self.sut.knot()
        assert(self.sut.list == [3, 4, 2, 1 0])
    """
