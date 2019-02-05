import pytest

from Generator import *

class TestGeneratorsWithoutCriteria(object):

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



class TestGeneratorsWithDivisonCriteria(object):

    @classmethod
    def setup(cls):
        def multipleOf4Criterion(number):
            return number % 4 == 0
        def multipleOf8Criterion(number):
            return number % 8 == 0
        cls.generatorA = Generator(65, 16807, criterion=multipleOf4Criterion)
        cls.generatorB = Generator(8921, 48271, criterion=multipleOf8Criterion)


    def test_generatorA_first_number_matches(self):
        expected_result = 1352636452
        result = next(self.generatorA.generate())
        assert result == expected_result


    def test_generatorA_fist_five_numbers_matches(self):
        expected_result = [1352636452, 1992081072, 530830436, 1980017072, 740335192]
        result = [next(self.generatorA.generate()) for i in range(5)]
        assert result == expected_result


    def test_generatorB_first_number_matches(self):
        expected_result = 1233683848
        result = next(self.generatorB.generate())
        assert result == expected_result


    def test_generatorB_fist_five_numbers_matches(self):
        expected_result = [1233683848, 862516352, 1159784568, 1616057672, 412269392]
        result = [next(self.generatorB.generate()) for i in range(5)]
        assert result == expected_result
