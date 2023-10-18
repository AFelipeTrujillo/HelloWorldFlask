import datetime

from flask import Flask, request, render_template, url_for, redirect, abort

app = Flask(__name__)

@app.route("/")
def hello_world():
    app.logger.info("this is an info msg")
    app.logger.error(f"this is an error msg {request.path}")
    return "<p>Hello, World! Andy</p>"

@app.route("/welcome/<name>")
def say_hi(name):
    return f"<p>Hey {name} !</p>"

@app.route("/years/<int:year>")
def say_years_old(year):
    today = datetime.date.today()
    current_year = today.year
    return f"<p>You are {current_year - year} years old</p>"

@app.route("/show/<name>", methods=['POST', 'GET'])
def show(name):
    return render_template('show.html', name = name)

@app.route("/redirect")
def do_redirect():
    return redirect(url_for('show', name='Joha'))

@app.route("/exit")
def do_exit():
    return abort(404)

@app.errorhandler(404)
def not_founf_page(error):
    return render_template('error404.html', error = error), 404 #thi is a tupla