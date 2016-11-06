from movie_rating.film_rank import FilmRank
import sys

if len(sys.argv) != 2:
    print "Usage:\n \tpython example.py {MOVIE_NAME}\n\n" \
          "Example:\n \tpython example.py 'A Separation'\n\n" \
          "You can also specify the movie's production year, like:\n" \
          "\tpython example.py 'Shawshank Redemption 1994'\n"
    exit()
movie_name = sys.argv[1].strip()
rater = FilmRank()
imdb_rating = rater.get_rating(movie_name)  # defaults to IMDB
print "{}, IMDB Rating: {}".format(movie_name, imdb_rating)
