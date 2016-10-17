#hosted on http://localhost:5000/login/

import sqlite3
from urllib.request import urlopen
from flask import Flask, render_template

app = Flask(__name__)

print("Enter the name of the database to access:")
db_access = input()

conn = sqlite3.connect(db_access)
print("\nAccessing database:", db_access)
print()

@app.route("/login/")
def login():	
	print("Redirecting to page 'INDEXLogin.html'")
	return render_template('INDEXLogin.html')