import sys
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import sqlite3
import os
import jinja2

app = Flask(__name__)
 
#root home
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('LOGIN.html')
    else:
        return render_template('HOME.html')

#movies page to display trending and accept query
@app.route('/movies')
def movies():
    return render_template('MOVIES.html')

#parsing request for search query
@app.route('/moviequery', methods=['POST'])
def moviequery():
    movie_found = False
    movie_name_query = request.form['moviereq']
    movie_name_query = movie_name_query.replace(" ","+")

    url_str = "http://www.omdbapi.com/?t=%s&y=&plot=full&r=json" % (movie_name_query)
    
    html = urlopen(url_str)
    html_doc_content = html.read()
    soup = BeautifulSoup(html_doc_content, 'html.parser')
    
    html_doc_hold = soup.get_text()

    html_doc_hold = '[' + html_doc_hold
    html_doc_hold = html_doc_hold + ']'

    fo = open("MOVIE_DATA.txt", "a")

    json_doc = json.loads(html_doc_hold)

    if(json_doc[0]['Response'] == 'False'):
        movie_found = False

    else:
        movie_found = True
        fo.write(json_doc[0]['Title'])
        fo.write("(")
        fo.write(json_doc[0]['Year'])
        fo.write(")")
        fo.write("\n")

    if movie_found == True:
        dict_movie = {'RD':json_doc[0]['Year'], 'R':json_doc[0]['Runtime'], 'G':json_doc[0]['Genre'], 'D':json_doc[0]['Director'], 'A':json_doc[0]['Actors'], 'I':json_doc[0]['imdbRating'], 'V':json_doc[0]['imdbVotes'], 'P':json_doc[0]['Plot']}

        return render_template('DISPLAY.html', dict_movie=dict_movie)

    else:
        return render_template('NOTFOUND.html')

#for accepting user feedback
@app.route('/faqentry', methods=['POST'])
def faqentry():
    name_response = request.form['name']
    email_response = request.form['email']
    experience_response = request.form['experience']

    flag = 0
    conn = sqlite3.connect('review.db')

    conn.execute(''' INSERT INTO REVIEWS VALUES("%s","%s","%s");''' % (name_response, email_response, experience_response))
    conn.commit()    


    return render_template('FAQ.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

@app.route('/aboutus')
def aboutus():
    return render_template('ABOUTUS.html')    
 
 #page for logging in
@app.route('/login', methods=['POST'])
def login():

    flag = 0
    conn = sqlite3.connect('sample.db')

    username_input = request.form['username']
    password_input = request.form['password']

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
            #print(row1[0])
            password_database = row1[0]

        if password_input == password_database:
            session['logged_in'] = True
            return home()

        else:            
            return home()

    else:
        return home()

#return home after sign up complete
@app.route('/signedin', methods=['POST'])
def signedin():

    flag = 0
    conn = sqlite3.connect('sample.db')

    username_input_signup = request.form['username']
    fullname_input_signup = request.form['fullname']
    email_input_signup = request.form['email']
    password_input_signup = request.form['password']

    conn.execute(''' INSERT INTO USERS VALUES ("%s","%s","%s","%s");''' % (fullname_input_signup, username_input_signup, password_input_signup, email_input_signup))
    conn.commit()

    return home()

#page for signing up
@app.route('/signup', methods=['POST'])
def signup():
    return render_template('SIGNUP.html')

#all logouts are sent to http://localhost:5000/logout
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()    
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)