import pytest
from exercise_sheet10 import *


def test_exercise_1a():
    answer = exercise_1a()
    expected = "a and b"
    assert answer == expected


def test_exercise_1b():
    answer = exercise_1b()
    expected = 1.5
    assert answer == expected


def test_exercise_1c():
    answer = exercise_1c()
    expected = 1
    assert answer == expected


def test_exercise_1d():
    answer = exercise_1d()
    expected = "c and d"
    assert answer == expected


def test_exercise_1e():
    answer = exercise_1e()
    matrix = [
        [0, 12.5, 9],  # {a,b}
        [12.5,    0, 7],  # {c,d}
        [9,  7, 0],  # e
    ]
    assert answer == matrix


def test_exercise_1f():
    answer = exercise_1f()
    expected = "((c : 3, d : 3) : 0.5, e : 3.5)"
    assert answer == expected


def test_exercise_1g():
    answer = exercise_1e()
    expected = "((a : 1.5, b : 1.5) : 4, ((c : 3, d : 3) : 0.5, e : 3.5) : 2);"
    assert answer == expected


def test_exercise_2a():
    one, two, three, four = exercise_2a()
    assert one is False
    assert two is False
    assert three is True
    assert four is True
