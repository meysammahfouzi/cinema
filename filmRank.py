from urllib import FancyURLopener
import urllib
import re
from bs4 import BeautifulSoup

import sys


class MyOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


def getRating(filmName):
    params = urllib.urlencode({'q': filmName + ' imdb'})
    opener = MyOpener()
    result = ""
    try:
        socket = opener.open('https://www.google.com/search?{}'.format(params))
    except IOError:
        print("no connection available!")
    else:
        result = socket.read()

    list = getListofFilms(result)

    firstIndex = result.find("Rating:")

    ratingIndex = firstIndex + len("Rating:")
    rating = result[ratingIndex:ratingIndex + 10].strip()
    p = re.compile(r"\d{1}\.?\d{0,2}/10")
    m = p.match(rating)

    if m:
        # print("rating: {}".format(m.group()))
        return m.group()
    else:
        print("no rating found for {}".format(filmName))
        return 0

def getListofFilms(html):
    soup = BeautifulSoup(html, "html.parser")
    imdbLinks = soup.select("div.slp")
    # return [h3.text for h3 in imdbLinks if re.search('imdb', h3.text, re.IGNORECASE)]
    return [h3.text for h3 in imdbLinks]
