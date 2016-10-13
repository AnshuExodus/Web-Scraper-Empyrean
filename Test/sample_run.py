import sqlite3

conn = sqlite3.connect('sample.db')
print("\nAccessing database: 'sample.db'")


cursor = conn.execute("SELECT * FROM Users;")

i = 1

for row in cursor:
	print("USER",i)
	print("------")
	print("Username: ", row[0])
	print("Password: ", row[1])	
	print("\n")
	i = i + 1

conn.close()