"""
Main script for AccentGuesser, a web app which uses machine learning to classify speech by accent.
Runs the web app, all other functionality is accessible through pages loaded in a browser.
Authors: Jillian MacGregor, Jonah Spicher, & Ashley Swanson
"""

import json
from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)

from werkzeug import secure_filename
from predict_class import main_given_filename

import os
from os.path import exists
import sys
import pickle
from pickle import dump, load

app = Flask(__name__)

lang='' #global variable for passing current accent guess between pages
filepath = ''

@app.route('/') #home page
def index():
    return render_template('index.html')


@app.route('/about') #takes user to github website
def about():
    return render_template('about.html')


@app.route('/record') #page where user records passage
def record():
    return render_template('audio_recorder/record.html')


@app.route('/r', methods = ['GET', 'POST']) #uploads file name for processing
def upload_file():
   if request.method == 'POST':
      try:
          f = request.files['file']
          f.save(secure_filename(f.filename))
          print(f)
      except:
          return redirect('/record')
      global lang #imports lang as a global variable
      global filepath
      print(f.filename)
      filepath = '../../Downloads/' + f.filename
      lang = main_given_filename(filepath)
      return redirect('/result')


@app.route('/result') #page with accent guess
def result():
    global lang #imports lang as a global variable
    return render_template('result.html', answer=lang)

@app.route('/answer', methods = ['GET', 'POST']) #uploads correct accent & audio
# file path to txt file for later trainings
def answer():
   if request.method == 'POST':
      first_lang = request.form['a']
      print(first_lang)

      file_name = 'AccentGuesserLearn.txt'
      global filepath
      if(exists(file_name) == False):
          f = open(file_name, 'wb')
          insert = pickle.dumps(first_lang + ' : ' + filepath + '\n')
          f.write(insert)
          f.close()

      else:
          f = open(file_name, 'rb+')
          curr = f.read()
          insert = pickle.dumps(first_lang + ' : ' + filepath + '\n')
          f.write(insert)
          f.close()

      return redirect('/result')


app.run(debug=True, host="0.0.0.0", port=8000)
