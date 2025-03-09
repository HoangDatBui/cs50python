from fuel import gauge, convert
from pytest import raises

def test_convert():
    assert convert("2/3") == 67
    with raises(ZeroDivisionError):
        convert("1/0")
    with raises(ValueError):
        convert("cat/dog")
    with raises(ValueError):
        convert("3/2")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"

