from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3


def insert_movie(newMovie, newYear, newPlot, newId, newReleased, newRuntime, newDirector, newWriter, newActors, newLanguage, newCountry, newAwards, newPoster, newMetascore, newImdbrating, newImdbvotes, newTotalseasons):

	conn = sqlite3.connect('Test.db')

	newIndex = return_existing_movie_count() + 1
	try:
		if newYear is not "" and newMovie is not "NULL_EXCEPTION":
			conn.execute(''' INSERT INTO MOVIE_LIST(movie_id,movie_name,movie_year,movie_plot,movie_imdbid,movie_released,movie_runtime,movie_director,movie_writer,movie_actors,movie_lanuage,movie_country,movie_awards,movie_poster,movie_metascore,movie_imdbrating,movie_imdbvotes,movie_totalseasons) VALUES("%d","%s","%s","%s");''' % (newIndex, newMovie, newYear, newPlot, newId, newReleased, newRuntime, newDirector, newWriter, newActors, newLanguage, newCountry, newAwards, newPoster, newMetascore, newImdbrating, newImdbvotes, newTotalseasons))
	except:
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
		omdb_plot = "NULL"

		omdb_id = "NULL"
		omdb_released = "NULL"
		omb_runtime =  "NULL"
		omdb_director = "NULL"
		omdb_writer = "NULL"
		omdb_actors = "NULL"
		omdb_language = "NULL"
		omdb_country = "NULL"
		omdb_awards = "NULL"
		omdb_poster = "NULL"
		omdb_metascore = "NULL"
		omdb_imdbrating = "NULL"
		omdb_imdbvotes = "NULL"
		omdb_type = "NULL"
		omdb_totalseasons = "NULL"

	else:
		omdb_name = json_doc[0]['Title']
		omdb_year = json_doc[0]['Year']	
		omdb_plot = json_doc[0]['Plot']

		omdb_id = json_doc[0]['imdbID']
		omdb_released = json_doc[0]['Released']
		omdb_runtime =  json_doc[0]['Runtime']
		omdb_director = json_doc[0]['Director']
		omdb_writer = json_doc[0]['Writer']
		omdb_actors = json_doc[0]['Actors']
		omdb_language = json_doc[0]['Language']
		omdb_country = json_doc[0]['Country']
		omdb_awards = json_doc[0]['Awards']
		omdb_poster = json_doc[0]['Poster']
		omdb_metascore = json_doc[0]['Metascore']
		omdb_imdbrating = json_doc[0]['imdbRating']
		omdb_imdbvotes = json_doc[0]['imdbVotes']
		omdb_type = json_doc[0]['Type']		

		if(json_doc[0]['Type'] == 'series'):
			omdb_totalseasons = json_doc[0]['totalSeasons']
		else:
			omdb_totalseasons = "NULL"
		

	return (omdb_name,omdb_year,omdb_plot,omdb_id,omdb_released,omdb_runtime,omdb_director,omdb_writer,omdb_actors,omdb_language,omdb_country,omdb_awards,omdb_poster,omdb_metascore,omdb_imdbrating,omdb_imdbvotes,omdb_totalseasons)


def return_existing_movie_count():
	conn = sqlite3.connect('Test.db')
	cursor = conn.execute("SELECT * FROM movie_list;")
	i = 0
	for row in cursor:
		i = i + 1
	return i

#return_existing_movie_count()	
#movie_request('movie_name')
#return_existing_movie_count()