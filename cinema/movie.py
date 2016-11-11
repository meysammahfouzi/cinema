# -*- coding: utf-8 -*-

from datetime import datetime

import requests
import requests_cache


class MovieNotFound(Exception):
    pass


class Movie(object):
    __api_url = 'http://www.omdbapi.com/?t=%s&y=&plot=full&r=json&tomatoes=true&type=movie&v=1'
    __headers = {'user-agent': 'cinema/0.0.1'}

    def __init__(self, name):
        assert type(name) is str

        name = name.strip()

        self._q = name
        self._title = None
        self._year = None
        self._released = None
        self._runtime = None
        self._genre = ()
        self._imdb_rating = None
        self._metascore = None
        self._tomatometer = None
        self._rated = None
        self._directors = ()
        self._writers = ()
        self._language = ()
        self._country = ()
        self._poster = None
        self._awards = None
        self._cast = ()
        self._plot = None
        self._imdb_id = None

        self._action()

    @property
    def title(self):
        """
        Title
        :type: str
        """
        return self._title

    @property
    def year(self):
        """
        Year
        :type: int
        """
        return self._year

    @property
    def released(self):
        """
        Year
        :type: date
        """
        return self._released

    @property
    def runtime(self):
        """
        Runtime
        :type: int
        """
        return self._runtime

    @property
    def genre(self):
        """
        Genre
        :type: tuple
        """
        return self._genre

    @property
    def imdb_rating(self):
        """
        IMDB Rating
        :type: float
        """
        return self._imdb_rating

    @property
    def metascore(self):
        """
        Metascore
        :type: int
        """
        return self._metascore

    @property
    def tomatometer(self):
        """
        TOMATOMETER
        :type: int
        """
        return self._tomatometer

    @property
    def rated(self):
        """
        Rated
        :type: str
        """
        return self._rated

    @property
    def directors(self):
        """
        Directors
        :type: tuple
        """
        return self._directors

    @property
    def writers(self):
        """
        Writers
        :type: tuple
        """
        return self._writers

    @property
    def language(self):
        """
        Language
        :type: tuple
        """
        return self._language

    @property
    def country(self):
        """
        Country
        :type: tuple
        """
        return self._country

    @property
    def poster(self):
        """
        Poster URL
        :type: str
        """
        return self._poster

    @property
    def awards(self):
        """
        Awards
        :type: str
        """
        return self._awards

    @property
    def cast(self):
        """
        Cast
        :type: tuple
        """
        return self._cast

    @property
    def plot(self):
        """
        Plot
        :type: str
        """
        return self._plot

    @property
    def imdb_id(self):
        """
        IMDB ID
        :type: str
        """
        return self._imdb_id

    def _action(self):
        requests_cache.install_cache('omdb_cache', expire_after=300, backend='memory')

        result = requests.get(self.__api_url % self._q, headers=self.__headers)

        if result.status_code != requests.codes.ok:
            raise ConnectionError

        data = result.json()
        if data['Response'] == 'False':
            raise MovieNotFound

        self._title = data['Title']
        self._imdb_rating = float(data['imdbRating'])
        self._metascore = int(data['Metascore'])
        self._tomatometer = int(data['tomatoMeter'])
        self._year = int(data['Year'])
        self._released = datetime.strptime(data['Released'], '%d %b %Y').date()
        self._runtime = int(data['Runtime'].split()[0])
        self._genre = tuple(data['Genre'].split(', '))
        self._directors = tuple(data['Director'].split(', '))
        self._writers = tuple(data['Writer'].split(', '))
        self._language = tuple(data['Language'].split(', '))
        self._country = tuple(data['Country'].split(', '))
        self._poster = data['Poster']
        self._rated = data['Rated']
        self._awards = data['Awards']
        self._cast = tuple(data['Actors'].split(', '))
        self._plot = data['Plot']
        self._imdb_id = data['imdbID']

    def __repr__(self):
        return 'Movie(%s - %d)' % (self.title, self.year)

    def __str__(self):
        return '%s (%d)' % (self.title, self.year)
