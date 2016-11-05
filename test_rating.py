"""This module contains tests for retrieving movie ratings."""

from filmRank import getRating

def test_1():
    """ Tests the rating of the movie called 'A Separation' """
    assert getRating("separation") == '8.4/10'

def test_2():
    """ Tests the rating of the movie called 'Shawshank Redemption' """
    assert getRating("shawshank redemption") == '9.3/10'

def test_3():
    """ Tests the rating of the movie called 'Sixth Sense' """
    assert getRating("sixth sense") == '8.1/10'
