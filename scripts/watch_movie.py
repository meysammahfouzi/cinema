#!/usr/bin/env python

import argparse

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
