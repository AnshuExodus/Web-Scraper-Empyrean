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
unique(movie_name, movie_year)
);

create table class_list (
movie_id integer,
genre_id integer,
primary key(movie_id, genre_id),
foreign key(movie_id) references movie_list(movie_id),
foreign key(genre_id) references genre_list(genre_id)
);
