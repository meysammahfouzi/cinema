# -*- coding: utf-8 -*-
from unittest import TestCase

from cinema.movie import Movie

class TestMovie(TestCase):
    def test_movie_name(self):
        self.assertEqual(Movie('the matrix revolutions').title, 'The Matrix Revolutions')

    def test_movie_director(self):
        self.assertEqual(Movie('A Separation').directors[0], 'Asghar Farhadi')