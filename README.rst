[![Build Status](https://travis-ci.org/meysammahfouzi/cinema.svg?branch=master)](https://travis-ci.org/meysammahfouzi/cinema)
[![Coverage Status](https://coveralls.io/repos/github/meysammahfouzi/cinema/badge.svg?branch=develop)](https://coveralls.io/github/meysammahfouzi/cinema?branch=develop)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
# Cinema
This python scripts retrieves the rating of a movie given its title.

The following web sites can be used to retreive the rating of movies:

- IMDB 
- RogerEbert 
- Metacritic

Currently only IMDB is supported but the support for the rest will be added soon.

## Installation
> pip install cinema  

or locally:

> python setup.py install

## Usage:
An example file has been added to indicate how to use the script. Note that you do not need to specify the movie's exact name.

> python example.py {MOVIE_NAME}  

Example:

> python example.py 'a separation'  

or  

> python example.py 'redemption'
