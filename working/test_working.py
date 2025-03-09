from working import convert
import pytest

def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')
def test_time():
    assert convert('10 PM to 5 AM') == '22:00 to 05:00'
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert('13 AM - 17 PM')
def test_wrong_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM - 9:60 PM')
