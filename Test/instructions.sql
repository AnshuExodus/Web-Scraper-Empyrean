sqlite>.header on
sqlite>.mode column
sqlite>.timer on

sqlite>.help
sqlite>.show


sqlite>.schema sqlite_master

CREATE TABLE sqlite_master (
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
);


IMPORTANT: How to attach from within database.



You can attach one and even more databases and work with it in the same way like using sqlite dbname.db

sqlite3
:
sqlite> attach "mydb.sqlite" as db1;

and you can see all attached databases with .databases

where in normal way the main is used for the command-line db

.databases
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main                                                                       
1    temp                                                                       
2    ttt              c:\home\user\gg.ite                                   






DATABASES
---------


testDB.db
---------

SELECT * FROM Users;


CREATE TABLE Users (
	username text,
	password text,
	PRIMARY KEY(username)
);


INSERT INTO Users (username, password) VALUES ('Isha', 1234);
INSERT INTO Users (username, password) VALUES ('Anshuman', 1234);


sample.db
---------

CREATE TABLE Sampling (
	username text,
	password text,
	PRIMARY KEY(username)
);


INSERT INTO Sampling (username, password) VALUES ('Isha', 1234);
INSERT INTO Sampling (username, password) VALUES ('Anshuman', 1234);