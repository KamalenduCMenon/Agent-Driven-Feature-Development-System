from features.is_prime import is_prime

def test_prime():
    assert is_prime(7) == True
    assert is_prime(4) == False