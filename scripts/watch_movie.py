#!/usr/bin/env python

import argparse

from requests import ConnectionError

from cinema.movie import Movie, MovieNotFound


def main():
    """The main routine."""
    parser = argparse.ArgumentParser(
        description="This python scripts retrieves the rating of a movie with its title. \n\texample: \n\t>> watch-movie 'lord of the rings' 2003")
    parser.add_argument("name", help="The name of movie you want to search")
    parser.add_argument("release_year", type=int, help='The release year of the movie.', nargs='?', default=0)
    parser.add_argument("-e", "--exact_match", action="store_true", help="search exact name of the movie.")

    args = parser.parse_args()

    try:
        movie = Movie(name=args.name, exact_match=args.exact_match, year=args.release_year)
        print(u"{} ({})".format(movie.title, movie.year))
        print(u"Awards: {}".format(movie.awards))
        print(u"IMDB Rating: {}/10".format(movie.imdb_rating))
        print(u"Tomato Meter: {}/100".format(movie.tomatometer))
        print(u"Meta Score: {}/100".format(movie.metascore))
        print(u"Director: {}".format(", ".join(movie.directors)))
        print(u"Cast: {}".format(", ".join(movie.cast)))
        print(u"Genre: {}".format(", ".join(movie.genre)))
        print(u"Country: {}".format(", ".join(movie.country)))
        print(u"Writer: {}".format(", ".join(movie.writers)))
        print(u"Language: {}".format(", ".join(movie.language)))
        print(u"Runtime: {}".format(movie.runtime))
        print(u"Released: {}".format(movie.released))
        print(u"Rated: {}".format(movie.rated))
        print(u"IMDB ID: {}".format(movie.imdb_id))
        print(u"Plot: {}".format(movie.plot))
    except MovieNotFound:
        print("No movie found!")
    except ConnectionError:
        print("No response!")

if __name__ == "__main__":
    main()
