from plates import is_valid

def test_alphabetical():
    assert is_valid("A1") == False
    assert is_valid("12CDEF") == False
    assert is_valid("1BCDEF") == False
    assert is_valid("AB") == True

def test_length():
    assert is_valid("ABCDEFG") == False

def test_start_num():
    assert is_valid("ABC123") == True
    assert is_valid("ABC012") == False

def test_middle_str():
    assert is_valid("ABC1P6") == False
    assert is_valid("ABC21P") == False

def test_alphanumeric():
    assert is_valid("ABC@#$") == False
