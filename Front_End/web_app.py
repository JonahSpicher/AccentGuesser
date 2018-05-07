import json
from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)

from werkzeug import secure_filename
from predict_class import main_given_filename

app = Flask(__name__)

lang='' #global variable for passing current accent guess between pages

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

      print(f.filename)
      filepath = '../../Downloads/' + f.filename
      global lang
      lang = main_given_filename(filepath)
      return render_template('result.html', answer=lang)


@app.route('/result') #page with accent guess
def result():
    return render_template('result.html')

@app.route('/answer', methods = ['GET', 'POST'])
def answer():
   if request.method == 'POST':
      first_lang = request.form['a']
      print(first_lang)
      global lang
      return render_template('result.html', answer=lang)


app.run(debug=True, host="0.0.0.0", port=8000)
