from um import count

def main():
    test_upper_lower_case()
    test_word_with_um()
    test_surrounded_by_space()

def test_upper_lower_case():
    assert count("Um, um...") == 2

def test_word_with_um():
    assert count("yummy") == 0

def test_surrounded_by_space():
    assert count(" um ") == 1
    
if __name__ == "__main__":
    main()
