.. image:: https://travis-ci.org/meysammahfouzi/cinema.svg?branch=master
    :target: https://travis-ci.org/meysammahfouzi/cinema
.. image:: https://coveralls.io/repos/github/meysammahfouzi/cinema/badge.svg?branch=master
    :target: https://coveralls.io/github/meysammahfouzi/cinema?branch=master

Cinema
------
This python scripts retrieves all the information of a movie given its title.
The following web sites are used to retrieve the rating of movies:

- IMDB 
- RogerEbert 
- Metacritic

Currently only IMDB is supported but the support for the rest will be added soon.

Installation
------------
    pip install cinema

or locally:

    python setup.py install

Usage:
------
After installing the package, you can use the following command to retrieve the information of a movie.
Note that you do not need to specify the movie's exact name.

    watch-movie {MOVIE_NAME}

Example:

    watch-movie 'a separation'

or  

    watch-movie 'redemption'

In case there are multiple versions of a movie, you can specify the production year too:

    watch-movie 'The Lord of the Rings' 2002