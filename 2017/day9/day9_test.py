import pytest
from day9 import *

class TestCleanGarbage(object):

    def test_remove_char(self):
        assert StreamProcessor().remove_char_from_string("aaabaa", 3) == "aaaaa"

    def test_1(self):
        assert StreamProcessor().clean_garbage("{<a>,<a>,<a>,<a>}") == "{,,,}"

    def test_2(self):
        assert StreamProcessor().clean_garbage("{{<a>},{<a>},{<a>},{<a>}}") == "{{},{},{},{}}"

    def test_3(self):
        assert StreamProcessor().clean_garbage("{{<!>},{<!>},{<!>},{<a>}}") == "{{}}"

    def test_4(self):
        assert StreamProcessor().clean_garbage("{{<!!>},{<!!>},{<!!>},{<!!>}}") == "{{},{},{},{}}"

class TestScoreForClearedStream(object):

    def test_1(self):
        assert StreamProcessor().count_score("{}") == 1

    def test_2(self):
        assert StreamProcessor().count_score("{{{}}}") == 6

    def test_3(self):
        assert StreamProcessor().count_score("{{},{}}") == 5

    def test_4(self):
        assert StreamProcessor().count_score("{{{},{},{{}}}}") == 16

    def test_5(self):
        assert StreamProcessor().count_score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9

    def test_6(self):
        assert StreamProcessor().count_score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9

    def test_7(self):
        assert StreamProcessor().count_score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3
