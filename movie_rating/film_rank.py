"""
This module provides functionality to retrieve
the rating of a movie from IMDB.
"""

import requests
import re
from bs4 import BeautifulSoup


class RatingReference(object):
    """ Enumeration """
    IMDB, RogerEbert, Metacritic = range(3)


class FilmRank(object):
    """
    Encapsulates the functionality of retrieving the rating of a movie from different sites.
    """

    def __init__(self, movie_dir="", rating_ref=RatingReference.IMDB):
        self.movie_dir = movie_dir
        self.movie_ref = rating_ref

    def get_rating(self, film_name):
        """
        Gets rating based on the reference rating site specified
        :param film_name: The name of the movie to get rating for
        :return: Rating of the movie
        """
        if self.movie_ref == RatingReference.IMDB:
            return self.get_rating_imdb(film_name)
        return ""

    def get_rating_imdb(self, film_name):
        """
        Retrieves the rating of a movie by its name
        :param film_name: Name of the movie
        :return: Its IMDB rating
        """
        payload = {'q': film_name + ' imdb'}
        result = ""
        try:
            r = requests.get('https://www.google.com/search', params=payload)
        except IOError:
            print "no connection available!"
        else:
            result = r.text

        first_index = result.find("Rating:")

        rating_index = first_index + len("Rating:")
        rating = result[rating_index:rating_index + 10].strip()
        pattern = re.compile(r"\d{1}\.?\d{0,2}/10")
        matched = pattern.match(rating)

        if matched:
            # print "rating: {}".format(matched.group())
            return matched.group()
        else:
            print "no rating found for {}".format(film_name)
            return 0
