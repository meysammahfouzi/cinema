# -*- coding: utf-8 -*-

import io

from setuptools import setup, find_packages


def readme():
    with io.open('README.rst', encoding='utf8') as f:
        return f.read()

ver = '0.0.11'

setup(
    name='cinema',
    packages=find_packages(),
    version=ver,
    description='Everything about Cinema!',
    long_description=readme(),
    author='Meysam Mahfouzi, Majid Hajiloo',
    author_email='maysam.mahfouzi@gmail.com, majid.hajiloo@gmail.com',
    url='https://github.com/meysammahfouzi/cinema',
    download_url='https://github.com/meysammahfouzi/cinema/tarball/' + ver,
    license='MIT',
    keywords=['movie', 'rating', 'imdb', 'film', 'cinema', 'actor', 'metascore', 'tomatometer'],
    install_requires=[
        'requests>=2,<3',
        'requests_cache>=0.4,<1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': ['watch-movie=scripts.watch_movie:main'],
    }
)
