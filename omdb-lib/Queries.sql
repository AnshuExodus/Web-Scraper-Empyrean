drop table class_list;
drop table genre_list;
drop table movie_list;

create table genre_list (
genre_id integer primary key,
genre_name varchar(30) unique not null
);

create table movie_list (
movie_id integer primary key,
movie_name varchar(30),
movie_year integer,
movie_plot text,

movie_imdbid text,
movie_released text,
movie_runtime text,
movie_director text,
movie_writer text,
movie_actors text,
movie_lanuage text,
movie_country text,
movie_awards text,
movie_poster text,
movie_metascore text,
movie_imdbrating text,
movie_imdbvotes text,
movie_totalseasons text,
unique(movie_name, movie_year)
);

create table class_list (
movie_id integer,
genre_id integer,
primary key(movie_id, genre_id),
foreign key(movie_id) references movie_list(movie_id),
foreign key(genre_id) references genre_list(genre_id)
);