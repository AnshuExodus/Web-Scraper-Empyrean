from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3


def insert_movie(newMovie, newYear):

	conn = sqlite3.connect('Movie.db')

	newIndex = return_existing_movie_count() + 1

	try:
		if movie_year_request is not "" and newMovie is not "NULL_EXCEPTION":
			conn.execute(''' INSERT INTO MOVIE_LIST VALUES("%d","%s","%s");''' % (newIndex, newMovie, newYear))
		elif newMovie is not "NULL_EXCEPTION":
			conn.execute(''' INSERT INTO MOVIE_LIST VALUES("%d","%s","%s");''' % (newIndex, newMovie, "NULL"))
		
	except:
		#print('')
		pass

	conn.commit()


def movie_request(movie_name_query, movie_year_request = ""):
	movie_name_query = movie_name_query.replace(" ","+")
	if movie_year_request is not "":
		url_str = "http://www.omdbapi.com/?t=%s&y=%s&plot=full&r=json" % (movie_name_query, movie_year_request)
		
	else:
		url_str = "http://www.omdbapi.com/?t=%s&y=&plot=full&r=json" % (movie_name_query)


	html = urlopen(url_str)
	html_doc_content = html.read()
	soup = BeautifulSoup(html_doc_content, 'html.parser')
	
	html_doc_hold = soup.get_text()

	html_doc_hold = '[' + html_doc_hold
	html_doc_hold = html_doc_hold + ']'

	json_doc = json.loads(html_doc_hold)

	if(json_doc[0]['Response'] == 'False'):
		#print("The movie you searched for doesn't exist.")
		omdb_name = "NULL_EXCEPTION"
		omdb_year = "NULL"
	else:
		omdb_name = json_doc[0]['Title']
		omdb_year = json_doc[0]['Year']		

	return (omdb_name,omdb_year)


def return_existing_movie_count():
	conn = sqlite3.connect('Movie.db')
	cursor = conn.execute("SELECT * FROM movie_list;")
	i = 0
	for row in cursor:
		i = i + 1
	return i


movie_name_query = input()
movie_year_request = input()

(omdb_movie_title, omdb_movie_year) = movie_request(movie_name_query)
movie_count = return_existing_movie_count()
insert_movie(omdb_movie_title, omdb_movie_year)

#print(movie_count+1)