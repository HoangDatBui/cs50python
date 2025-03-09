from bank import value

def test_capital():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_phrase():
    assert value("Hi, how are you?") == 20
    assert value("Morning, how are you?") == 100
