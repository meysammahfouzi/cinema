from cinema.movie import Movie, MovieNotFound
import sys

if len(sys.argv) != 2:
    print "Usage:\n \tpython example.py {MOVIE_NAME}\n\n" \
          "Example:\n \tpython example.py 'A Separation'\n\n" \
          "You can also specify the movie's production year, like:\n" \
          "\tpython example.py 'Shawshank Redemption 1994'\n"
    exit()

movie_name = sys.argv[1].strip()

try:
    movie = Movie(movie_name)
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


