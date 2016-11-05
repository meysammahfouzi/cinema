"""This module contains tests for retrieving movie ratings."""

from film_rank import get_rating


def test_1():
    """ Tests the rating of the movie called 'A Separation' """
    assert get_rating("separation") == '8.4/10'


def test_2():
    """ Tests the rating of the movie called 'Shawshank Redemption' """
    assert get_rating("shawshank redemption") == '9.3/10'


def test_3():
    """ Tests the rating of the movie called 'Sixth Sense' """
    assert get_rating("sixth sense") == '8.1/10'
