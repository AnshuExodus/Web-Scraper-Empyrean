import sqlite3

print("Enter database name to access:")

db_access = input()
#db_access: sample.db

conn = sqlite3.connect(db_access)
print("\nAccessing database:", db_access)
print()

"""
conn.execute('''CREATE TABLE Users (
	full_name text,
	username text,
	password text,
	email text,
	PRIMARY KEY(username)
);''')

"""



#print("\nTABLE Users created")


"""
conn.execute("INSERT INTO Users (full_name, username, password, email) VALUES ('Isha Sinha', 'Isha', '1234', 'ishsinha@gmail.com');")
conn.execute("INSERT INTO Users (full_name, username, password, email) VALUES ('Anshuman Mishra', 'Anshuman', '1234', 'anshumanjoeymishra@gmail.com');")
conn.commit()

"""


#print("\nVALUES inserted in Users\n")

cursor = conn.execute("SELECT * FROM Users;")

i = 1

for row in cursor:
	print("USER",i)
	print("------")
	print("Username: ", row[1])	
	print("Password: ", row[2])	
	print("\n")
	i = i + 1

point = conn.execute("SELECT * FROM Users;")

j = 1

#Dumps the login credentials into Data.txt
#Opening the file in append mode to record every login instance
fo = open("Data.txt", "a")
#print("Accessing:", fo.name)

for row in point:
	fo.write("Full name: ")
	fo.write(row[0])
	fo.write("\n")
	fo.write("Username: ")
	fo.write(row[1])
	fo.write("\n")
	fo.write("Password: ")
	fo.write(row[2])
	fo.write("\n")
	fo.write("Email ID: ")
	fo.write(row[3])	
	fo.write("\n\n")
	j = j + 1

fo.close()
conn.close()