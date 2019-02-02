import pytest

from MultipleRounds import *

class TestMultipleRounds(object):

    @classmethod
    def setup(cls):
        cls.sut = MultipleRounds()
        cls.list = list(range(256))

    def test_convert_ASCII(self):
        assert(self.sut.convert_ASCII("1,2,3") == [49,44,50,44,51])

    def test_get_input_length(self):
        result = self.sut.get_input_length("1,2,3")
        assert(result == [49,44,50,44,51,17,31,73,47,23])

    def test_after_64_rounds_with_length_1_series_1_2_is_the_same(self):
        self.sut.knotHash = KnotHash([1, 2], [1])
        assert(self.sut.run_rounds() == [1, 2])

    def test_after_64_rounds_with_length_2_series_1_2_is_reverted(self):
        self.sut.knotHash = KnotHash([1, 2], [2])
        assert(self.sut.run_rounds() == [2, 1])

    def test_dense_hash(self):
        input = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        assert(self.sut.dense_hash_block(input) == 64)

    def test_dense_hase_of_two_blocks(self):
        input = [65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        assert(self.sut.dense_hash(input) == [65, 121])

    def test_convert_output_to_hex(self):
        input = [10, 1]
        assert(self.sut.convert_to_hex(input) == "a1")

    def test_hash_empty_string(self):
        expected = "a2582a3a0e66e6e86e3812dcb672a272"
        assert(self.sut.calc_hash(self.list, "") == expected)
