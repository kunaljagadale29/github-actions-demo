from app import add, subtract, multiply


def test_add():
    assert add(2, 3) == 7


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 5) == 15
