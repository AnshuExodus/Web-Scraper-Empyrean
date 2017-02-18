from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3


def genre_request(genre_name):
	conn = sqlite3.connect('Movie.db')
	
	try:
		movie_names = conn.execute(''' SELECT MOVIE_NAME FROM MOVIE_LIST
			WHERE MOVIE_ID IN (
			SELECT MOVIE_ID FROM CLASS_LIST
			WHERE GENRE_ID IN (
			SELECT GENRE_ID FROM GENRE_LIST WHERE GENRE_NAME = "%s")); ''' % (genre_name))

		for row in movie_names:
			print(row[0])

	except:
		pass

	conn.commit()
	conn.close()

genre_request('Horror')

def movie_desc(movie_name):
	conn = sqlite3.connect('Movie.db')

	try:
		movie_plot = conn.execute(''' SELECT MOVIE_PLOT FROM MOVIE_LIST WHERE MOVIE_NAME = "%s"; ''' %(movie_name))
		for row in movie_plot:
			print(row[0])

	except:
		pass

	conn.commit()
	conn.close()

#movie_desc('Movie_Name')			