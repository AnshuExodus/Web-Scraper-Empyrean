from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json
import sqlite3

conn = sqlite3.connect('Movie.db')

cursor_g = conn.execute("SELECT * FROM genre_list;")
cursor_m = conn.execute("SELECT * FROM movie_list;")
cursor_c = conn.execute("SELECT * FROM class_list;")

for row in cursor_g:
	print("Genre ID: ", row[0])	
	print("Genre Name: ", row[1])	
	print("\n")

for row in cursor_m:
	print("Movie ID: ", row[0])	
	print("Movie Name: ", row[1])	
	print("\n")

for row in cursor_c:
	print("Class ID: ", row[0])	
	print("Movie ID: ", row[1])	
	print("Genre ID: ", row[2])
	print("\n")		

conn.close()