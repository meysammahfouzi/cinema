"""
This module provides functionality to retrieve
the rating of a movie from IMDB.
"""

from urllib import FancyURLopener
import urllib
import re
from bs4 import BeautifulSoup


class MyOpener(FancyURLopener, object):
    """
    This class helps in sending query to HTTPS pages
    """
    version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) " \
              "Gecko/20071127 Firefox/2.0.0.11"


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
        self.opener = MyOpener()

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
        params = urllib.urlencode({'q': film_name + ' imdb'})
        result = ""
        try:
            socket = self.opener.open('https://www.google.com/search?{}'.format(params))
        except IOError:
            print "no connection available!"
        else:
            result = socket.read()

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

    def __get_list_of_films(self, html):
        """
        Returns list of films available in the HTML provided
        :param html: The HTML string containing list of movies
        :return: List of movie titles
        """
        soup = BeautifulSoup(html, "html.parser")
        imdb_links = soup.select("div.slp")
        # return [h3.text for h3 in imdb_links
        #         if re.search('imdb', h3.text, re.IGNORECASE)]
        return [h3.text for h3 in imdb_links]
