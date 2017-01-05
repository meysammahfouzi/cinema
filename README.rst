.. image:: https://travis-ci.org/meysammahfouzi/cinema.svg?branch=master
    :target: https://travis-ci.org/meysammahfouzi/cinema
.. image:: https://coveralls.io/repos/github/meysammahfouzi/cinema/badge.svg?branch=master
    :target: https://coveralls.io/github/meysammahfouzi/cinema?branch=master

Cinema
------
This python scripts retrieves the rating of a movie given its title.
The following web sites are used to retreive the rating of movies:

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
An example file has been added to indicate how to use the script. Note that you do not need to specify the movie's exact name.

    python example.py {MOVIE_NAME}  

Example:

    python example.py 'a separation'  

or  

    python example.py 'redemption'
