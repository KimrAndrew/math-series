from math_series.math_series import fibonacci, lucas
import pytest

def test_fib():
    assert fibonacci

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fib_30():
    actual = fibonacci(30)
    expected = 832040
    assert actual == expected

def test_luc():
    assert lucas


def test_fib_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_luc_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_luc_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_luc_30():
    actual = lucas(30)
    expected = 1860498
    assert actual == expected