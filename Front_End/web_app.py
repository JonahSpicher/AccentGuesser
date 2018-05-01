import json
from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)

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


@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('character', json.dumps(dict(request.form.items())))
    return response


@app.route('/test')
def test():
    return render_template('audio_recorder/ar.html')


app.run(debug=True, host="0.0.0.0", port=8000)
