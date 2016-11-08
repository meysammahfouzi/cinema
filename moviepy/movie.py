# -*- coding: utf-8 -*-

class BaseMoviePy(object):
    def __init__(self, name):
        assert type(name) is str

        self._q = name
        self._name = None
        self._rating = None
        self._directors = ()
        self._awards = ()
        self._cast = ()
        self._plot = None
        self._url = None
        self.rating_range = ()
        self.service_url = None

    @property
    def name(self):
        return self._name

    @property
    def rating(self) -> float:
        if self._rating is None:
            self._rating = self.get_rating()

        return self._rating

    @property
    def directors(self):
        return self._directors

    @property
    def awards(self):
        return self._awards

    @property
    def cast(self):
        return self._cast

    @property
    def plot(self):
        return self._plot

    @property
    def url(self):
        return self._url

    def get_rating(self):
        raise NotImplementedError

    def __repr__(self):
        return 'MoviePy(%s)' % self.name

    def __str__(self):
        return self.__repr__()
