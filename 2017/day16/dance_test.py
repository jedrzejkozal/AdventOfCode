import pytest

from main import *


def test_spin():
    string = "a b c d e".split()
    output, _, _, _ = dance("s2", string)
    assert output == ['d', 'e', 'a', 'b', 'c']


def test_exchange():
    string = "a b c d e".split()
    output, _, _, _ = dance("x1/2", string)
    assert output == ['a', 'c', 'b', 'd', 'e']


def test_partner():
    string = "a b c d e".split()
    output, _, _, _ = dance("pb/e", string)
    assert output == ['a', 'e', 'c', 'd', 'b']


def test_right_output():
    f = open('input.txt')
    input = f.read()
    f.close()

    string = "a b c d e f g h i j k l m n o p".split()
    output, _, _, _ = dance(input, string)
    assert output == ['o', 'c', 'i', 'e', 'd', 'p', 'j',
                      'b', 'm', 'f', 'n', 'k', 'h', 'l', 'g', 'a']
