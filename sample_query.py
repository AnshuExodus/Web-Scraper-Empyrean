import sys
import os
import sqlite3

flag = 0
conn = sqlite3.connect('sample.db')

print("Enter username: ")

username_input = input()

cursor = conn.execute(''' SELECT COUNT(PASSWORD) FROM USERS WHERE USERNAME = "%s"; ''' % (username_input))

for row0 in cursor:
	if row0[0] == 0:
		flag = 0
	else:
		flag = 1

#print("Flag",flag)		

if flag == 1:
	cursor = conn.execute(''' SELECT PASSWORD FROM USERS WHERE USERNAME = "%s"; ''' % (username_input))

	for row1 in cursor:
		print(row1[0])

else:
	print("The user doesn't exist.")




