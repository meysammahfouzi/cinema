# -*- coding: utf-8 -*-
from unittest import TestCase

from cinema.movie import Movie


class TestMovie(TestCase):
    def test_movie_name(self):
        self.assertEqual(Movie('the matrix revolutions').title, 'The Matrix Revolutions')

    def test_movie_director(self):
        self.assertEqual(Movie('A Separation').directors[0], 'Asghar Farhadi')

    def test_imdb_rating(self):
        self.assertEqual(Movie('shawshank redemption').imdb_rating, 9.3)

    def test_movie_year(self):
        self.assertEqual(Movie('sixth sense').year, 1999)

    def test_movie_cast(self):
        self.assertEqual(", ".join(Movie('matrix').cast), "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving")

    def test_movie_cast(self):
        self.assertEqual(Movie('match point').imdb_id, 'tt0416320')
