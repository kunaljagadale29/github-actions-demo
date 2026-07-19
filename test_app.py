from app import add, subtract, multiply


def test_add():
    assert add(7, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 5) == 15
