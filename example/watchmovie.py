from cinema.movie import Movie, MovieNotFound
import sys

if len(sys.argv) < 2:
    print "Usage:\n \twatchmovie.py {MOVIE_NAME} {RELEASE_YEAR}\n" \
          "\tThe RELEASE_YEAR parameter is optional\n" \
          "Example:\n \twatchmovie.py 'A Separation'\n\n" \
          "You can also specify the movie's production year:\n" \
          "\twatchmovie.py 'lord of the rings' 2003\n"
    exit()

movie_name = sys.argv[1].strip()
release_year = 0
if len(sys.argv) == 3:
    release_year = int(sys.argv[2].strip())

try:
    movie = Movie(movie_name, exact_match=False, year=release_year)
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


