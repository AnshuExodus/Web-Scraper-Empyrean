from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print("\n\nEnter movie to search for: ")
movie_name_query = input()

print("\nMOVIE INFORMATION\n")
print("-------------------\n")

movie_name_query = movie_name_query.replace(" ","+")

url_str = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" %movie_name_query

html = urlopen(url_str)
html_doc_content = html.read()
soup = BeautifulSoup(html_doc_content, 'html.parser')

#print(html_doc_content)
#print(soup.prettify())

html_doc_hold = soup.get_text()
print(html_doc_hold)

#Obtain position of poster URL
find_poster_pos = html_doc_hold.find("\"Poster\"")
#print(find_poster_pos)



