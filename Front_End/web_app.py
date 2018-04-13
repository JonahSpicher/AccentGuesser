import json
from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/save', methods=['POST'])
# def save():
#   response = make_response(redirect(url_for('index')))
#   response.set_cookie('character', json.dumps(dict(request.form.items())))
#   return response

app.run(debug=True, host="0.0.0.0", port=8000)
