from Judge import *


class TestJudge(object):

    def setup(cls):
        generatorA = Generator(65, 16807)
        generatorB = Generator(8921, 48271)
        cls.sut = Judge(generatorA, generatorB)


    def test_number_of_matching_numbers_for_simple_example_from_AoC_is_1(self):
        expected_result = 1
        result = self.sut.calculateCount(comparisons=5)
        assert expected_result == result


    def test_number_of_matching_numbers_for_example_from_AoC_is_588(self):
        expected_result = 588
        result = self.sut.calculateCount()
        assert expected_result == result
