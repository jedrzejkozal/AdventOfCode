import pytest

from day3 import *

class TestUlamSprial(object):

    #  1   9  25  49   81
    #  1   3   5   7    9
    #
    #  0   1   2   3    4

    def test_position_of_1_is_0_0(self):
        s = UlamSprial()
        assert s.getPositionOfBegining(1) == (0, 0)

    def test_position_of_9_is_1_1(self):
        s = UlamSprial()
        assert s.getPositionOfBegining(9) == (1, -1)

    def test_position_of_25_is_2_2(self):
        s = UlamSprial()
        assert s.getPositionOfBegining(25) == (2, -2)

    def test_position_of_49_is_3_3(self):
        s = UlamSprial()
        assert s.getPositionOfBegining(49) == (3, -3)

    def test_position_of_81_is_4_4(self):
        s = UlamSprial()
        assert s.getPositionOfBegining(81) == (4, -4)

    def test_begining_for_4_is_9(self):
        s = UlamSprial()
        assert s.getValueOfBeginingForSomeNumber(4) == 9

    def test_begining_for_7_is_9(self):
        s = UlamSprial()
        assert s.getValueOfBeginingForSomeNumber(7) == 9

    def test_begining_for_12_is_25(self):
        s = UlamSprial()
        assert s.getValueOfBeginingForSomeNumber(12) == 25

    def test_begining_for_20_is_25(self):
        s = UlamSprial()
        assert s.getValueOfBeginingForSomeNumber(20) == 25

    def test_corners_for_25(self):
        s = UlamSprial()
        assert s.getCornersForBegin(25) == (25, 21, 17, 13)

    def test_position_of_20_is_3(self):
        s = UlamSprial()
        assert s.getPositionOfNumber(20) == 3

    def test_position_of_43_is_6(self):
        s = UlamSprial()
        assert s.getPositionOfNumber(43) == 6

    def test_position_of_32_is_5(self):
        s = UlamSprial()
        assert s.getPositionOfNumber(32) == 5

    def test_position_of_46_is_3(self):
        s = UlamSprial()
        assert s.getPositionOfNumber(46) == 3
