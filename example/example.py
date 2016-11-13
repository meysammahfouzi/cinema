from cinema.movie import Movie
import sys

if len(sys.argv) != 2:
    print "Usage:\n \tpython example.py {MOVIE_NAME}\n\n" \
          "Example:\n \tpython example.py 'A Separation'\n\n" \
          "You can also specify the movie's production year, like:\n" \
          "\tpython example.py 'Shawshank Redemption 1994'\n"
    exit()

movie_name = sys.argv[1].strip()
movie = Movie(movie_name)
print("Title: {}".format(movie.title))
print("Director: {}".format(movie.directors))
print("Country: {}".format(movie.country))
print("Awards: {}".format(movie.awards))
print("Genre: {}".format(movie.genre))
print("IMDB Rating: {}".format(movie.imdb_rating))
