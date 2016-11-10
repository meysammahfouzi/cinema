# -*- coding: utf-8 -*-
import re

import requests

from moviepy.movie import BaseMoviePy


class IMDB(BaseMoviePy):
    def __init__(self, name):
        super(IMDB, self).__init__(name)

        self._name = name
        self.rating_range = (0, 10)
        self.service_url = 'http://imdb.com'

        self.__rating_cache = 0

    def get_rating(self):
        if self.__rating_cache > 0:
            return None

        self.__rating_cache += 1

        payload = {'q': self._q + ' imdb'}

        r = requests.get('https://www.google.com/search', params=payload)
        if r.status_code == requests.codes.ok:
            result = r.text
        else:
            raise ValueError('Response is not OK', r.status_code)

        first_index = result.find("Rating:")

        rating_index = first_index + len("Rating:")
        rating = result[rating_index:rating_index + 10].strip()
        pattern = re.compile(r"\d{1}\.?\d{0,2}/10")
        matched = pattern.match(rating)

        if matched:
            return matched.group()  # it must be float!
        else:
            raise ValueError("No rating found", self._q)
