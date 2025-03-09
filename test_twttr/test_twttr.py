from twttr import shorten

def test_lowercase():
    assert shorten("lmao") == "lm"

def test_uppercase():
    assert shorten("LMAO") == "LM"

def test_number():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("?!.,") == "?!.,"
