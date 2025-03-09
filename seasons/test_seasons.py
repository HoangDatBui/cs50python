import pytest
from seasons import calculate_minutes, convert_to_words

def test_calculate_minutes():
    assert calculate_minutes("1999-01-01") == 525600
    assert calculate_minutes("1999-12-31") == 1440
    assert calculate_minutes("1970-01-01") == 15778080

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(1440) == "One thousand, four hundred forty"
    assert convert_to_words(15778080) == "Fifteen million, seven hundred seventy-eight thousand eighty"

def test_invalid_date():
    with pytest.raises(ValueError):
        calculate_minutes("invalid-date")
