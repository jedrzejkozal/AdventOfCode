import pytest

from day2 import *

class TestChecksumDiffCalculator(object):

    @pytest.fixture(scope="function")
    def resource_calc(self):
        return ChecksumDiffCalculator()

    def test_find_min_and_max_for_empty_list_min_is_Inf_max_is_zero(self, resource_calc):
        c = self.resource_calc()
        min, max = c.find_min_and_max([])
        assert min == float('inf')
        assert max == 0

    def test_find_min_and_max_for_1_2_3_4_will_min_1_max_4(self, resource_calc):
        c = self.resource_calc()
        min, max = c.find_min_and_max([1,2,3,4])
        assert min == 1
        assert max == 4

    def test_find_min_and_max_for_100_257_3_412_114_56_will_min_3_max_412(self, resource_calc):
        c = self.resource_calc()
        min, max = c.find_min_and_max([100,257,3,412,114,56])
        assert min == 3
        assert max == 412

    def test_calculate_diffrence_for_5_1_9_5_will_return_8(self, resource_calc):
        c = self.resource_calc()
        assert c.calculate_row_diffrence([5,1,9,5]) == 8

    def test_calculate_diffrence_for_7_5_3_will_return_4(self, resource_calc):
        c = self.resource_calc()
        assert c.calculate_row_diffrence([7,5,3]) == 4

    def test_calculate_diffrence_for_2_4_6_8_will_return_8(self, resource_calc):
        c = self.resource_calc()
        assert c.calculate_row_diffrence([2,4,6,8]) == 6

    def test_array(self):
        c = self.resource_calc()
        assert c.calculate_checksum_diffrence([[5,1,9,5],[7,5,3],[2,4,6,8]]) == 18

class TestChecksumDivCalculator:

    @pytest.fixture(scope="function")
    def resource_calc(self):
        return ChecksumDivCalculator()

    def test_find_two_divisable_numbers_for_empty_returns_None(self, resource_calc):
        c = self.resource_calc()
        assert c.find_two_divisable_numbers([]) == None

    def test_find_two_divisable_numbers_for_2_3_4_5_returns_2_4(self, resource_calc):
        c = self.resource_calc()
        assert c.find_two_divisable_numbers([2,3,4,5]) == (2, 4)

    def test_find_two_divisable_numbers_for_16_7_10_5_3_2_returns_16_2(self, resource_calc):
        c = self.resource_calc()
        assert c.find_two_divisable_numbers([16,7,10,5,3,2]) == (16, 2)
