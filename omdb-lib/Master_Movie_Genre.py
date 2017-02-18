import Movie_Manager
import Genre_Manager
import sqlite3

def link_movie_genre(movie_name, movie_year, genre_name):
	conn = sqlite3.connect('Test.db')
	
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
	(master_movie_name,master_movie_year,master_movie_plot,master_movie_id,master_movie_released,master_movie_runtime,master_movie_director,master_movie_writer,master_movie_actors,master_movie_language,master_movie_country,master_movie_awards,master_movie_poster,master_movie_metascore,master_movie_imdbrating,master_movie_imdbvotes,master_movie_totalseasons) = Movie_Manager.movie_request(movie_name, movie_year)
	#print("###" + master_movie_name)
	Movie_Manager.insert_movie(master_movie_name,master_movie_year,master_movie_plot,master_movie_id,master_movie_released,master_movie_runtime,master_movie_director,master_movie_writer,master_movie_actors,master_movie_language,master_movie_country,master_movie_awards,master_movie_poster,master_movie_metascore,master_movie_imdbrating,master_movie_imdbvotes,master_movie_totalseasons)

	genres = Genre_Manager.genre_request(movie_name)

	if genres is not None:

		for genre in genres:	
			Genre_Manager.insert_genre(genre.strip())
			link_movie_genre(master_movie_name, master_movie_year, genre.strip())

#master('Movie_Name')			