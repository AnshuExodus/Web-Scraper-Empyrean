from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3

def return_genre():

	conn = sqlite3.connect('Movie.db')

	cursor = conn.execute("SELECT * FROM genre_list;")
	return cursor

genre_store = return_genre()

for row in genre_store:
	print(row[1])