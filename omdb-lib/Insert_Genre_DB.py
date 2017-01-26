from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3

movie_name_query = input()

def insert_genre(newGenre):

	conn = sqlite3.connect('Movie.db')

	newIndex = return_existing_genre_count() + 1

	try:
		conn.execute(''' INSERT INTO GENRE_LIST VALUES("%d","%s");''' % (newIndex, newGenre))
		
	except:
		#print('')
		pass

	conn.commit()


def genre_request(movie_name_query):
	movie_name_query = movie_name_query.replace(" ","+")
	url_str = "http://www.omdbapi.com/?t=%s&y=&plot=full&r=json" % (movie_name_query)

	html = urlopen(url_str)
	html_doc_content = html.read()
	soup = BeautifulSoup(html_doc_content, 'html.parser')
	
	html_doc_hold = soup.get_text()

	html_doc_hold = '[' + html_doc_hold
	html_doc_hold = html_doc_hold + ']'

	json_doc = json.loads(html_doc_hold)

	genre_data = None
	if(json_doc[0]['Response'] == 'False'):
		print("The movie you searched for doesn't exist.")
		
	else:
		genre_data = (json_doc[0]['Genre']).split(",")
	
	return genre_data


def return_genre():

	conn = sqlite3.connect('Movie.db')

	cursor = conn.execute("SELECT * FROM genre_list;")
	return cursor

def return_existing_genre_count():
	genre_store = return_genre()
	i = 0
	for row in genre_store:
		i = i + 1
	return i

#insert_genre("MyNewGenre")
#insert_genre("MyNewGenre2")

genres = genre_request(movie_name_query)

if genres is not None:

	for genre in genres:	
		insert_genre(genre.strip())
