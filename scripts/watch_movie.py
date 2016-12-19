#!/usr/bin/env python

import argparse

from cinema.movie import Movie, MovieNotFound


def main():
    """The main routine."""
    parser = argparse.ArgumentParser(usage="usage: %prog [options]",
                                     description='This python scripts retrieves the rating of a movie with its title',
                                     prog='watch_movie')
    parser.add_argument("-n", "--name", help="The name of movie you want to search", type=str)
    parser.add_argument("--ry", "--release_year", type=int, help='The release year of the movie.', default=0)
    parser.add_argument("--em", "--exact_match", action="store_true", default=False,
                        help="search exact name of the movie.")

    args = parser.parse_args()

    if len(args) < 1:
        parser.error("Type 'watch-movie.py --help <option>' for help on a specific option."
                     "\nUsage:\n \twatch-movie.py --name --release_year\n"
                     "\texample: \n\twatch-movie.py -n 'lord of the rings' -ry 2003\n")

    try:
        movie = Movie(name=args.name.strip(), exact_match=args.exact_match, year=args.release_year)
        print("{} ({})".format(movie.title, movie.year))
        print("Awards: {}".format(movie.awards))
        print("IMDB Rating: {}/10".format(movie.imdb_rating))
        print("Tomato Meter: {}/100".format(movie.tomatometer))
        print("Meta Score: {}/100".format(movie.metascore))
        print("Director: {}".format(", ".join(movie.directors)))
        print("Cast: {}".format(", ".join(movie.cast)))
        print("Genre: {}".format(", ".join(movie.genre)))
        print("Country: {}".format(", ".join(movie.country)))
        print("Writer: {}".format(", ".join(movie.writers)))
        print("Language: {}".format(", ".join(movie.language)))
        print("Runtime: {}".format(movie.runtime))
        print("Released: {}".format(movie.released))
        print("Rated: {}".format(movie.rated))
        print("IMDB ID: {}".format(movie.imdb_id))
        print("Plot: {}".format(movie.plot))
    except MovieNotFound:
        print("No movie found!")


if __name__ == "__main__":
    main()
