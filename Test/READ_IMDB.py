from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

print("\n\nEnter movie to search for: ")
movie_name_query = input()
print("\n\nWould you like a summarized or detailed plot? (short/full): ")
plot_request_query = input()

flag = 0

if(plot_request_query != 'short' and plot_request_query != 'full'):
	flag = 1
	print("\nInvalid plot request: Enter (short/full) only.")	
	exit()

print("\nMOVIE INFORMATION\n")
print("-------------------\n")

movie_name_query = movie_name_query.replace(" ","+")

url_str = "http://www.omdbapi.com/?t=%s&y=&plot=%s&r=json" % (movie_name_query, plot_request_query)

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

fo = open("MOVIE_DATA.txt", "a")

json_doc = json.loads(html_doc_hold)

if(json_doc[0]['Response'] == 'False'):
	print("The movie you searched for doesn't exist.")	

else:
	fo.write(json_doc[0]['Title'])
	fo.write("(")
	fo.write(json_doc[0]['Year'])
	fo.write(")")
	fo.write("\n")

	print("Release Date:", json_doc[0]['Released'])
	print("\n")
	print("Runtime:", json_doc[0]['Runtime'])
	print("\n")
	print("Genre:", json_doc[0]['Genre'])
	print("\n")
	print("Director:", json_doc[0]['Director'])
	print("\n")
	print("Cast:", json_doc[0]['Actors'])
	print("\n")
	print("IMDb Rating:", json_doc[0]['imdbRating'], "out of", json_doc[0]['imdbVotes'], "votes")
	print("\n")
	print("Plot Summary:", json_doc[0]['Plot'])
	print("\n")

fo.close()
