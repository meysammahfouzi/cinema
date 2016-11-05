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


def get_rating(film_name):
    """
    Retrieves the rating of a movie by its name
    :param film_name: Name of the movie
    :return: Its IMDB rating
    """
    params = urllib.urlencode({'q': film_name + ' imdb'})
    opener = MyOpener()
    result = ""
    try:
        socket = opener.open('https://www.google.com/search?{}'.format(params))
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


def __get_list_of_films(html):
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
