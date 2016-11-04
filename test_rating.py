from filmRank import getRating

def test_1():
    assert getRating("separation") == '8.4/10'

def test_2():
    assert getRating("shawshank redemption") == '9.3/10'

def test_3():
    assert getRating("sixth sense") == '8.1/10'