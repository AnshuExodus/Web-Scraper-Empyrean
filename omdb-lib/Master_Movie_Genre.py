import Movie_Manager
import Genre_Manager
import sqlite3

def link_movie_genre(movie_name, movie_year, genre_name):
	conn = sqlite3.connect('Movie.db')
	
	try:
		conn.execute(''' INSERT INTO CLASS_LIST (MOVIE_ID, GENRE_ID)
		SELECT MOVIE_LIST.MOVIE_ID, GENRE_LIST.GENRE_ID
		FROM MOVIE_LIST, GENRE_LIST
		WHERE MOVIE_LIST.MOVIE_NAME="%s"
		AND MOVIE_LIST.MOVIE_YEAR="%s"
		AND GENRE_LIST.GENRE_NAME="%s"; ''' % (movie_name, movie_year, genre_name))

	except:
		pass

	conn.commit()



def master(movie_name, movie_year = ""):
	(master_movie_name, master_movie_year) = Movie_Manager.movie_request(movie_name, movie_year)
	#print("###" + master_movie_name)
	Movie_Manager.insert_movie(master_movie_name, master_movie_year)

	genres = Genre_Manager.genre_request(movie_name)

	if genres is not None:

		for genre in genres:	
			Genre_Manager.insert_genre(genre.strip())
			link_movie_genre(master_movie_name, master_movie_year, genre.strip())

master('raees')			