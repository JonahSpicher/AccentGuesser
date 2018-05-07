import json
from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)

from werkzeug import secure_filename
from predict_class import main_given_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/record')
def record():
    return render_template('audio_recorder/record.html')


@app.route('/r', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      try:
          f = request.files['file']
          f.save(secure_filename(f.filename))
          print(f)
      except:
          return redirect('/record')

      #JJ do some stuff
      #print(f.filename)
      filepath = '../../Desktop/' + f.filename
      lang = main_given_filename(filepath)

      #lang = 'Danish'
      return render_template('result.html', answer=lang)


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/answer', methods = ['GET', 'POST'])
def answer():
   if request.method == 'POST':
      first_lang = request.form['a']
      print(first_lang)
      return redirect('/result')


app.run(debug=True, host="0.0.0.0", port=8000)
