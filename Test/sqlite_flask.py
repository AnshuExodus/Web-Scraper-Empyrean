#local copy of testDB.db at C:\Users\Admin\Desktop\Semester V\Projects\ITT\Database (SQLite)

import sqlite3

conn = sqlite3.connect('testDB.db')
print("Accessing Database: testDB.db")


conn.execute('''CREATE TABLE Users (
	username text,
	password text,
	PRIMARY KEY(username)
);''')



conn.execute('''INSERT INTO Users (username, password) VALUES ('Isha', 1234);''')

conn.execute('''INSERT INTO Users (username, password) VALUES ('Anshuman', 1234);''')

conn.execute("SELECT * FROM Users;")

conn.close()

