#!/usr/bin/python
# -*- coding: utf-8 -*-

# imports media and fresh_tomatoes python files

import media
import fresh_tomatoes

# Instantiates 6 movie objects

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://bit.ly/1qM8Na0',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'http://bit.ly/1O2b493',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

ai = media.Movie('AI',
                 'A robotic boy embarks on a journey to find his true self',
                 'http://bit.ly/2yC0GET',
                 'https://www.youtube.com/watch?v=oBUAQGwzGk0')

rat = media.Movie('Ratatouille',
                  'A rat who loves tasting food and befriends a cook',
                  'http://bit.ly/2xTg1l0',
                  'https://www.youtube.com/watch?v=c3sBBRxDAqk')

indiana = media.Movie('Indiana Jones: The Last Crusade',
                      'Indiana Jones goes on a quest',
                      'http://bit.ly/2ytvPdR',
                      'https://www.youtube.com/watch?v=a6JB2suJYHM')

wonder = media.Movie('Wonder Woman',
                     'She fights a war to end all wars',
                     'http://bit.ly/2rRZASN',
                     'https://www.youtube.com/watch?v=VSB4wGIdDwo')

# Makes a list of movie objects

movies = [
    toy_story,
    avatar,
    ai,
    rat,
    indiana,
    wonder,
    ]

# uses fresh_tomatoes.py to make a website that displays all the movies.

fresh_tomatoes.open_movies_page(movies)
