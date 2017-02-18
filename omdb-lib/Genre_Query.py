from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

movie_name_query = input()

def genre_request(movie_name_query):

	#print("\n\nEnter movie to search for: ")	

	movie_name_query = movie_name_query.replace(" ","+")

	url_str = "http://www.omdbapi.com/?t=%s&y=&plot=full&r=json" % (movie_name_query)

	html = urlopen(url_str)
	html_doc_content = html.read()
	soup = BeautifulSoup(html_doc_content, 'html.parser')

	#print(html_doc_content)
	#print(soup.prettify())
	
	html_doc_hold = soup.get_text()
	#print(html_doc_hold)

	html_doc_hold = '[' + html_doc_hold
	html_doc_hold = html_doc_hold + ']'
	#print(html_doc_hold)

	#fo = open("MOVIE_DATA.txt", "a")

	json_doc = json.loads(html_doc_hold)

	if(json_doc[0]['Response'] == 'False'):
		print("The movie you searched for doesn't exist.")	

	else:
		#fo.write(json_doc[0]['Title'])
		#fo.write("(")
		#fo.write(json_doc[0]['Year'])
		#fo.write(")")
		#fo.write("\n")

		#Output the genre(s) of the movie

		#print(json_doc[0]['Genre'])
		#print("\n")

		genre_data = (json_doc[0]['Genre']).split(",")
		return genre_data

	#fo.close()

genre_request_return = genre_request(movie_name_query)

for row in genre_request_return:
	print(row.strip())