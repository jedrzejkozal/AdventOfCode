import pytest

from main import *


def test_buffer_after_0_steps_have_zero_only():
    buffer = spinlock(step=3, num_steps=0)
    assert buffer == [0]


def test_after_first_step_buffer_state_is_0_1():
    buffer = spinlock(step=3, num_steps=1)
    assert buffer == [0, 1]


def test_after_2_steps_buffer_state_is_0_2_1():
    buffer = spinlock(step=3, num_steps=2)
    assert buffer == [0, 2, 1]


def test_after_3_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=3)
    assert buffer == [0, 2, 3, 1]


def test_after_4_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=4)
    assert buffer == [0, 2, 4, 3, 1]


def test_after_5_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=5)
    assert buffer == [0, 5, 2, 4, 3, 1]


def test_after_6_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=6)
    assert buffer == [0, 5, 2, 4, 3, 6, 1]


def test_after_7_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=7)
    assert buffer == [0, 5, 7, 2, 4, 3, 6, 1]


def test_after_8_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=8)
    assert buffer == [0, 5, 7, 2, 4, 3, 8, 6, 1]


def test_after_9_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=9)
    assert buffer == [0, 9, 5, 7, 2, 4, 3, 8, 6, 1]


def test_after_2017_steps_buffer_state_is_correct():
    buffer = spinlock(step=3, num_steps=2017)
    index = buffer.index(2017)
    index = (index+1) % len(buffer)
    assert buffer[index] == 638
