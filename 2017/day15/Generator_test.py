import pytest

from Generator import *

class TestGenerators(object):

    @classmethod
    def setup(cls):
        cls.generatorA = Generator(65, 16807)
        cls.generatorB = Generator(8921, 48271)


    def test_generatorA_first_number_matches(self):
        expected_result = 1092455
        result = next(self.generatorA.generate())
        assert result == expected_result


    def test_generatorA_fist_five_numbers_matches(self):
        expected_result = [1092455, 1181022009, 245556042, 1744312007, 1352636452]
        result = [next(self.generatorA.generate()) for i in range(5)]
        assert result == expected_result


    def test_generatorB_first_number_matches(self):
        expected_result = 430625591
        result = next(self.generatorB.generate())
        assert result == expected_result


    def test_generatorB_fist_five_numbers_matches(self):
        expected_result = [430625591, 1233683848, 1431495498, 137874439, 285222916]
        result = [next(self.generatorB.generate()) for i in range(5)]
        assert result == expected_result
