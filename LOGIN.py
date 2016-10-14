#hosted on http://localhost:5000/login/

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/login/")
def login():	
	return render_template('INDEXLogin.html')

@app.route("/home/")
def home():
	return 'home'

@app.route("/trending/")
def trending():
	return 'trending'
	
if __name__ == "__main__":
	app.run(debug = True)	