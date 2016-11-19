import sqlite3

print("Enter database name to access:")

db_access = input()
#db_access: review.db

conn = sqlite3.connect(db_access)
print("\nAccessing database:", db_access)
print()

"""
conn.execute('''CREATE TABLE Reviews (
	full_name text,
	email text,
	feedback text,	 
	PRIMARY KEY(email)
);''')

"""

conn.commit()

print("\nTABLE Reviews created")

conn.execute("INSERT INTO Reviews (full_name, email, feedback) VALUES ('Isha Sinha', 'ishsinha@gmail.com', 'My new IMdB');")
conn.execute("INSERT INTO Reviews (full_name, email, feedback) VALUES ('Anshuman Mishra', 'anshumanjoeymishra@gmail.com', 'Does the job well');")
conn.commit()

print("\nVALUES inserted in Users\n")