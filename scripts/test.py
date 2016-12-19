import argparse

parser = argparse.ArgumentParser(usage="usage: %prog [options]",
                                 description='This python scripts retrieves the rating of a movie with its title')
parser.add_argument("-n", "--name", help="The name of movie you want to search", type=str)
parser.add_argument("--ry", "--release_year", type=int, help='The release year of the movie.', default=0)
parser.add_argument("--em", "--exact_match", action="store_true", default=False,
                    help="search exact name of the movie.")

args = parser.parse_args()
print(args.accumulate(args.name))
