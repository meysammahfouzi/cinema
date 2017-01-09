# -*- coding: utf-8 -*-
from unittest import TestCase

import datetime

from cinema.movie import Movie


class TestMovie(TestCase):
    def test_movie_name(self):
        self.assertEqual(Movie('the matrix revolutions').title, 'The Matrix Revolutions')

    def test_movie_director(self):
        self.assertEqual(", ".join(Movie('A Separation').directors), 'Asghar Farhadi')

    def test_imdb_rating_1(self):
        self.assertEqual(Movie('shawshank redemption').imdb_rating, 9.3)

    def test_imdb_rating_2(self):
        self.assertEqual(Movie('redemption').imdb_rating, 9.3)

    def test_imdb_rating_3(self):
        self.assertEqual(Movie("The Lord of the Rings", exact_match=False, year=2001).imdb_rating, 8.8)

    def test_imdb_rating_4(self):
        self.assertEqual(Movie("The Lord of the Rings", exact_match=False, year=2002).imdb_rating, 8.7)

    def test_imdb_rating_5(self):
        self.assertEqual(Movie("The Lord of the Rings", exact_match=False, year=2003).imdb_rating, 8.9)

    def test_imdb_rating_6(self):
        self.assertEqual(Movie("The Lord of the Rings", exact_match=False, year=1978).imdb_rating, 6.2)

    def test_movie_year(self):
        self.assertEqual(Movie('sixth sense').year, 1999)

    def test_movie_cast(self):
        self.assertEqual(", ".join(Movie('matrix').cast),
                         "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving")

    def test_movie_imdb_id(self):
        self.assertEqual(Movie('match point').imdb_id, 'tt0416320')

    def test_movie_genre(self):
        self.assertEqual(", ".join(Movie('godfather').genre), 'Crime, Drama')

    def test_movie_awards(self):
        self.assertEqual(Movie('12 Angry Men').awards, 'Nominated for 3 Oscars. Another 16 wins & 8 nominations.')

    def test_movie_country(self):
        self.assertEqual(", ".join(Movie("schindler's list").country), 'USA')

    def test_movie_language(self):
        self.assertEqual(", ".join(Movie("pulp fiction").language), 'English, Spanish, French')

    def test_movie_writers(self):
        self.assertEqual(", ".join(Movie("fight club").writers), 'Chuck Palahniuk (novel), Jim Uhls (screenplay)')

    def test_movie_writers2(self):
        self.assertEqual(", ".join(Movie("test").writers), 'Nicholas Gyeney (story), Nicholas Gyeney, André Kirkman')

    def test_movie_tomato_meter(self):
        self.assertEqual(Movie("star wars", exact_match=False, year=1980).tomatometer, 94)

    def test_movie_tomato_plot(self):
        self.assertEqual(Movie("Forrest Gump").plot,
                         "Forrest Gump is a simple man with a low I.Q. but good intentions. "
                         "He is running through childhood with his best and only friend Jenny. "
                         "His 'mama' teaches him the ways of life and leaves him to choose his destiny. "
                         "Forrest joins the army for service in Vietnam, finding new friends called Dan "
                         "and Bubba, he wins medals, creates a famous shrimp fishing fleet, inspires people "
                         "to jog, starts a ping-pong craze, creates the smiley, writes bumper stickers and songs, "
                         "donates to people and meets the president several times. However, this is all "
                         "irrelevant to Forrest who can only think of his childhood sweetheart Jenny Curran, "
                         "who has messed up her life. Although in the end all he wants to prove is that "
                         "anyone can love anyone.")

    def test_fallback_to_google_1(self):
        self.assertEqual(Movie('forushande').title, 'The Salesman')

    def test_fallback_to_google_2(self):
        self.assertEqual(Movie('like love kiarostami').title, 'Like Someone in Love')

    def test_fallback_to_google_3(self):
        self.assertEqual(", ".join(Movie('so far so near mirkarimi').writers), 'Mohammad Reza Gohari, Reza Mirkarimi')

    def test_unicode_actor(self):
        self.assertEqual(", ".join(Movie('like love kiarostami').cast), u'Tadashi Okuno, Rin Takanashi, Ryô Kase, Denden')

    def test_release(self):
        self.assertEqual(Movie('godfather', year=1972).released, datetime.date(1972, 3, 24))

    def test_runtime(self):
        self.assertEqual(Movie('godfather', year=1990).runtime, 162)

    def test_meta_score(self):
        self.assertEqual(Movie('shawshank redemption').metascore, 80)

    def test_rated(self):
        self.assertEqual(Movie('fight club').rated, 'R')

    # def test_exact_match(self):
    #     self.assertEqual(Movie('fight club', exact_match=True).title, 'Fight Club')

    def test_str(self):
        self.assertEqual(str(Movie('godfather', year=1972)), "The Godfather (1972)")

    def test_repr(self):
        self.assertEqual(repr(Movie('godfather', year=1972)), "Movie(The Godfather - 1972)")
